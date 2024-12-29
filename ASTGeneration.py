from CompiledFiles.SampleParser import SampleParser
from CompiledFiles.SampleVisitor import SampleVisitor
from ASTUtils import *

class ASTGeneration(SampleVisitor):
    def visitProgram(self, ctx: SampleParser.ProgramContext):
        statements = [stmt.accept(self) for stmt in ctx.statement()]
        return Program(statements)

    def visitStatement(self, ctx: SampleParser.StatementContext):
        if ctx.selectStmt():
            return ctx.selectStmt().accept(self)
        elif ctx.updateStmt():
            return ctx.updateStmt().accept(self)
        elif ctx.insertStmt():
            return ctx.insertStmt().accept(self)
        elif ctx.getChild(0).getText() == 'read':
            return self.visitChildren(ctx)
        elif ctx.getChild(0).getText() == 'display':
            return self.visitChildren(ctx)
        else:
            return self.visitChildren(ctx)

    def visitSelectStmt(self, ctx: SampleParser.SelectStmtContext):
        columns = [col.getText() for col in ctx.columns().ID()]
        table = ctx.ID().getText()
        condition = ctx.condition().accept(self)
        return Select(columns, table, condition)

    def visitUpdateStmt(self, ctx: SampleParser.UpdateStmtContext):
        table = ctx.ID().getText()
        assignment = ctx.assignment().accept(self)
        condition = ctx.condition().accept(self)
        return Update(table, assignment, condition)

    def visitInsertStmt(self, ctx: SampleParser.InsertStmtContext):
        table = ctx.ID().getText()
        columns = [col.getText() for col in ctx.columns().ID()]
        values = [val.accept(self) for val in ctx.values().value()]
        return Insert(table, columns, values)

    def visitAssignment(self, ctx: SampleParser.AssignmentContext):
        column = ctx.ID().getText()
        value = ctx.value().accept(self)
        return Assignment(column, value)

    def visitCondition(self, ctx: SampleParser.ConditionContext):
        column = ctx.ID().getText()
        comparator = ctx.comparator().getText()
        value = ctx.value().accept(self)
        return Condition(column, comparator, value)

    def visitValue(self, ctx: SampleParser.ValueContext):
        if ctx.STRING():
            return Value(ctx.STRING().getText().strip('"'))
        elif ctx.INTEGER():
            return Value(int(ctx.INTEGER().getText()))