# Generated from Sample.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SampleParser import SampleParser
else:
    from SampleParser import SampleParser

# This class defines a complete generic visitor for a parse tree produced by SampleParser.

class SampleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SampleParser#program.
    def visitProgram(self, ctx:SampleParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#statement.
    def visitStatement(self, ctx:SampleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#selectStmt.
    def visitSelectStmt(self, ctx:SampleParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#updateStmt.
    def visitUpdateStmt(self, ctx:SampleParser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#insertStmt.
    def visitInsertStmt(self, ctx:SampleParser.InsertStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#columns.
    def visitColumns(self, ctx:SampleParser.ColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#values.
    def visitValues(self, ctx:SampleParser.ValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#assignment.
    def visitAssignment(self, ctx:SampleParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#condition.
    def visitCondition(self, ctx:SampleParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#value.
    def visitValue(self, ctx:SampleParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#comparator.
    def visitComparator(self, ctx:SampleParser.ComparatorContext):
        return self.visitChildren(ctx)



del SampleParser