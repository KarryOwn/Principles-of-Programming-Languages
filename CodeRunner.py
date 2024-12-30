import pandas as pd
from ASTUtils import *

class CodeRunner:
    def visitProgram(self, ctx: Program):
        results = []
        for statement in ctx.statements:
            result = statement.accept(self)
            results.append(result)
        return results

    def visitSelect(self, ctx: Select):
        data = self.load_data(ctx.table)
        condition_func = self.create_condition_func(ctx.condition.column)(ctx.condition.comparator)(ctx.condition.value.value)
        result = data[data.apply(condition_func, axis=1)][ctx.columns]
        return result.to_dict(orient='records')

    def visitUpdate(self, ctx: Update):
        data = self.load_data(ctx.table)
        condition_func = self.create_condition_func(ctx.condition.column)(ctx.condition.comparator)(ctx.condition.value.value)
        assignment_func = self.create_assignment_func(ctx.assignment.value.value)
        data.loc[data.apply(condition_func, axis=1), ctx.assignment.column] = assignment_func(None)
        self.save_data(ctx.table, data)
        return "Update successful"

    def visitInsert(self, ctx: Insert):
        data = self.load_data(ctx.table)
        new_row = {col: val.value for col, val in zip(ctx.columns, ctx.values)}
        new_row_df = pd.DataFrame([new_row])
        data = pd.concat([data, new_row_df], ignore_index=True)
        self.save_data(ctx.table, data)
        return "Insert successful"

    def create_condition_func(self, column):
        def comparator_func(comparator):
            if comparator == '=':
                comparator = '=='
            def value_func(value):
                return eval(f"lambda row: row['{column}'] {comparator} {value}")
            return value_func
        return comparator_func

    def create_assignment_func(self, value):
        return lambda _: value

    def load_data(self, table):
        return pd.read_excel(f"{table}.xlsx")

    def save_data(self, table, data):
        data.to_excel(f"{table}.xlsx", index=False)