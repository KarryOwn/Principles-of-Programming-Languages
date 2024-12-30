# Generated from Sample.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,83,8,6,10,6,12,6,86,9,6,1,7,
        1,7,1,7,5,7,91,8,7,10,7,12,7,94,9,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,2,2,0,23,23,25,25,1,0,18,22,103,0,25,1,0,0,0,2,42,1,0,0,0,4,
        44,1,0,0,0,6,52,1,0,0,0,8,60,1,0,0,0,10,72,1,0,0,0,12,79,1,0,0,0,
        14,87,1,0,0,0,16,95,1,0,0,0,18,99,1,0,0,0,20,103,1,0,0,0,22,105,
        1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,1,1,0,0,0,29,43,3,4,2,0,30,43,3,6,3,0,31,43,3,8,
        4,0,32,43,3,10,5,0,33,34,5,1,0,0,34,35,5,2,0,0,35,36,5,23,0,0,36,
        37,5,3,0,0,37,38,5,24,0,0,38,43,5,4,0,0,39,40,5,5,0,0,40,41,5,24,
        0,0,41,43,5,4,0,0,42,29,1,0,0,0,42,30,1,0,0,0,42,31,1,0,0,0,42,32,
        1,0,0,0,42,33,1,0,0,0,42,39,1,0,0,0,43,3,1,0,0,0,44,45,5,6,0,0,45,
        46,3,12,6,0,46,47,5,7,0,0,47,48,5,24,0,0,48,49,5,8,0,0,49,50,3,18,
        9,0,50,51,5,4,0,0,51,5,1,0,0,0,52,53,5,9,0,0,53,54,5,24,0,0,54,55,
        5,10,0,0,55,56,3,16,8,0,56,57,5,8,0,0,57,58,3,18,9,0,58,59,5,4,0,
        0,59,7,1,0,0,0,60,61,5,11,0,0,61,62,5,12,0,0,62,63,5,24,0,0,63,64,
        5,13,0,0,64,65,3,12,6,0,65,66,5,14,0,0,66,67,5,15,0,0,67,68,5,13,
        0,0,68,69,3,14,7,0,69,70,5,14,0,0,70,71,5,4,0,0,71,9,1,0,0,0,72,
        73,5,16,0,0,73,74,5,7,0,0,74,75,5,24,0,0,75,76,5,8,0,0,76,77,3,18,
        9,0,77,78,5,4,0,0,78,11,1,0,0,0,79,84,5,24,0,0,80,81,5,17,0,0,81,
        83,5,24,0,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,
        0,0,85,13,1,0,0,0,86,84,1,0,0,0,87,92,3,20,10,0,88,89,5,17,0,0,89,
        91,3,20,10,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,
        0,0,93,15,1,0,0,0,94,92,1,0,0,0,95,96,5,24,0,0,96,97,5,18,0,0,97,
        98,3,20,10,0,98,17,1,0,0,0,99,100,5,24,0,0,100,101,3,22,11,0,101,
        102,3,20,10,0,102,19,1,0,0,0,103,104,7,0,0,0,104,21,1,0,0,0,105,
        106,7,1,0,0,106,23,1,0,0,0,4,27,42,84,92
    ]

class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'from'", "'as'", "';'", "'display'", 
                     "'SELECT'", "'FROM'", "'WHERE'", "'UPDATE'", "'SET'", 
                     "'INSERT'", "'INTO'", "'('", "')'", "'VALUES'", "'DELETE'", 
                     "','", "'='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "ID", 
                      "INTEGER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_updateStmt = 3
    RULE_insertStmt = 4
    RULE_deleteStmt = 5
    RULE_columns = 6
    RULE_values = 7
    RULE_assignment = 8
    RULE_condition = 9
    RULE_value = 10
    RULE_comparator = 11

    ruleNames =  [ "program", "statement", "selectStmt", "updateStmt", "insertStmt", 
                   "deleteStmt", "columns", "values", "assignment", "condition", 
                   "value", "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    STRING=23
    ID=24
    INTEGER=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SampleParser.StatementContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SampleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 68194) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStmt(self):
            return self.getTypedRuleContext(SampleParser.SelectStmtContext,0)


        def updateStmt(self):
            return self.getTypedRuleContext(SampleParser.UpdateStmtContext,0)


        def insertStmt(self):
            return self.getTypedRuleContext(SampleParser.InsertStmtContext,0)


        def deleteStmt(self):
            return self.getTypedRuleContext(SampleParser.DeleteStmtContext,0)


        def STRING(self):
            return self.getToken(SampleParser.STRING, 0)

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SampleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.selectStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.updateStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.insertStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.deleteStmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.match(SampleParser.T__0)
                self.state = 34
                self.match(SampleParser.T__1)
                self.state = 35
                self.match(SampleParser.STRING)
                self.state = 36
                self.match(SampleParser.T__2)
                self.state = 37
                self.match(SampleParser.ID)
                self.state = 38
                self.match(SampleParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.match(SampleParser.T__4)
                self.state = 40
                self.match(SampleParser.ID)
                self.state = 41
                self.match(SampleParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columns(self):
            return self.getTypedRuleContext(SampleParser.ColumnsContext,0)


        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def condition(self):
            return self.getTypedRuleContext(SampleParser.ConditionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_selectStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = SampleParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SampleParser.T__5)
            self.state = 45
            self.columns()
            self.state = 46
            self.match(SampleParser.T__6)
            self.state = 47
            self.match(SampleParser.ID)
            self.state = 48
            self.match(SampleParser.T__7)
            self.state = 49
            self.condition()
            self.state = 50
            self.match(SampleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def assignment(self):
            return self.getTypedRuleContext(SampleParser.AssignmentContext,0)


        def condition(self):
            return self.getTypedRuleContext(SampleParser.ConditionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_updateStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStmt" ):
                return visitor.visitUpdateStmt(self)
            else:
                return visitor.visitChildren(self)




    def updateStmt(self):

        localctx = SampleParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_updateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SampleParser.T__8)
            self.state = 53
            self.match(SampleParser.ID)
            self.state = 54
            self.match(SampleParser.T__9)
            self.state = 55
            self.assignment()
            self.state = 56
            self.match(SampleParser.T__7)
            self.state = 57
            self.condition()
            self.state = 58
            self.match(SampleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def columns(self):
            return self.getTypedRuleContext(SampleParser.ColumnsContext,0)


        def values(self):
            return self.getTypedRuleContext(SampleParser.ValuesContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_insertStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStmt" ):
                return visitor.visitInsertStmt(self)
            else:
                return visitor.visitChildren(self)




    def insertStmt(self):

        localctx = SampleParser.InsertStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_insertStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SampleParser.T__10)
            self.state = 61
            self.match(SampleParser.T__11)
            self.state = 62
            self.match(SampleParser.ID)
            self.state = 63
            self.match(SampleParser.T__12)
            self.state = 64
            self.columns()
            self.state = 65
            self.match(SampleParser.T__13)
            self.state = 66
            self.match(SampleParser.T__14)
            self.state = 67
            self.match(SampleParser.T__12)
            self.state = 68
            self.values()
            self.state = 69
            self.match(SampleParser.T__13)
            self.state = 70
            self.match(SampleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def condition(self):
            return self.getTypedRuleContext(SampleParser.ConditionContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_deleteStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStmt" ):
                return visitor.visitDeleteStmt(self)
            else:
                return visitor.visitChildren(self)




    def deleteStmt(self):

        localctx = SampleParser.DeleteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_deleteStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SampleParser.T__15)
            self.state = 73
            self.match(SampleParser.T__6)
            self.state = 74
            self.match(SampleParser.ID)
            self.state = 75
            self.match(SampleParser.T__7)
            self.state = 76
            self.condition()
            self.state = 77
            self.match(SampleParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.ID)
            else:
                return self.getToken(SampleParser.ID, i)

        def getRuleIndex(self):
            return SampleParser.RULE_columns

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumns" ):
                return visitor.visitColumns(self)
            else:
                return visitor.visitChildren(self)




    def columns(self):

        localctx = SampleParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(SampleParser.ID)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 80
                self.match(SampleParser.T__16)
                self.state = 81
                self.match(SampleParser.ID)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.ValueContext)
            else:
                return self.getTypedRuleContext(SampleParser.ValueContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = SampleParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.value()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 88
                self.match(SampleParser.T__16)
                self.state = 89
                self.value()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(SampleParser.ValueContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SampleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SampleParser.ID)
            self.state = 96
            self.match(SampleParser.T__17)
            self.state = 97
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SampleParser.ID, 0)

        def comparator(self):
            return self.getTypedRuleContext(SampleParser.ComparatorContext,0)


        def value(self):
            return self.getTypedRuleContext(SampleParser.ValueContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = SampleParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SampleParser.ID)
            self.state = 100
            self.comparator()
            self.state = 101
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SampleParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(SampleParser.INTEGER, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = SampleParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not(_la==23 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_comparator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = SampleParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





