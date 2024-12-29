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
        4,1,25,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,73,8,5,
        10,5,12,5,76,9,5,1,6,1,6,1,6,5,6,81,8,6,10,6,12,6,84,9,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,
        10,12,14,16,18,20,0,2,2,0,22,22,24,24,1,0,17,21,93,0,23,1,0,0,0,
        2,39,1,0,0,0,4,41,1,0,0,0,6,49,1,0,0,0,8,57,1,0,0,0,10,69,1,0,0,
        0,12,77,1,0,0,0,14,85,1,0,0,0,16,89,1,0,0,0,18,93,1,0,0,0,20,95,
        1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,1,1,0,0,0,27,40,3,4,2,0,28,40,3,6,3,0,29,40,3,8,
        4,0,30,31,5,1,0,0,31,32,5,2,0,0,32,33,5,22,0,0,33,34,5,3,0,0,34,
        35,5,23,0,0,35,40,5,4,0,0,36,37,5,5,0,0,37,38,5,23,0,0,38,40,5,4,
        0,0,39,27,1,0,0,0,39,28,1,0,0,0,39,29,1,0,0,0,39,30,1,0,0,0,39,36,
        1,0,0,0,40,3,1,0,0,0,41,42,5,6,0,0,42,43,3,10,5,0,43,44,5,7,0,0,
        44,45,5,23,0,0,45,46,5,8,0,0,46,47,3,16,8,0,47,48,5,4,0,0,48,5,1,
        0,0,0,49,50,5,9,0,0,50,51,5,23,0,0,51,52,5,10,0,0,52,53,3,14,7,0,
        53,54,5,8,0,0,54,55,3,16,8,0,55,56,5,4,0,0,56,7,1,0,0,0,57,58,5,
        11,0,0,58,59,5,12,0,0,59,60,5,23,0,0,60,61,5,13,0,0,61,62,3,10,5,
        0,62,63,5,14,0,0,63,64,5,15,0,0,64,65,5,13,0,0,65,66,3,12,6,0,66,
        67,5,14,0,0,67,68,5,4,0,0,68,9,1,0,0,0,69,74,5,23,0,0,70,71,5,16,
        0,0,71,73,5,23,0,0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,
        75,1,0,0,0,75,11,1,0,0,0,76,74,1,0,0,0,77,82,3,18,9,0,78,79,5,16,
        0,0,79,81,3,18,9,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,
        83,1,0,0,0,83,13,1,0,0,0,84,82,1,0,0,0,85,86,5,23,0,0,86,87,5,17,
        0,0,87,88,3,18,9,0,88,15,1,0,0,0,89,90,5,23,0,0,90,91,3,20,10,0,
        91,92,3,18,9,0,92,17,1,0,0,0,93,94,7,0,0,0,94,19,1,0,0,0,95,96,7,
        1,0,0,96,21,1,0,0,0,4,25,39,74,82
    ]

class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'from'", "'as'", "';'", "'display'", 
                     "'SELECT'", "'FROM'", "'WHERE'", "'UPDATE'", "'SET'", 
                     "'INSERT'", "'INTO'", "'('", "')'", "'VALUES'", "','", 
                     "'='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "ID", "INTEGER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_updateStmt = 3
    RULE_insertStmt = 4
    RULE_columns = 5
    RULE_values = 6
    RULE_assignment = 7
    RULE_condition = 8
    RULE_value = 9
    RULE_comparator = 10

    ruleNames =  [ "program", "statement", "selectStmt", "updateStmt", "insertStmt", 
                   "columns", "values", "assignment", "condition", "value", 
                   "comparator" ]

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
    STRING=22
    ID=23
    INTEGER=24
    WS=25

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2658) != 0)):
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.selectStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.updateStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.insertStmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(SampleParser.T__0)
                self.state = 31
                self.match(SampleParser.T__1)
                self.state = 32
                self.match(SampleParser.STRING)
                self.state = 33
                self.match(SampleParser.T__2)
                self.state = 34
                self.match(SampleParser.ID)
                self.state = 35
                self.match(SampleParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.match(SampleParser.T__4)
                self.state = 37
                self.match(SampleParser.ID)
                self.state = 38
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
            self.state = 41
            self.match(SampleParser.T__5)
            self.state = 42
            self.columns()
            self.state = 43
            self.match(SampleParser.T__6)
            self.state = 44
            self.match(SampleParser.ID)
            self.state = 45
            self.match(SampleParser.T__7)
            self.state = 46
            self.condition()
            self.state = 47
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
            self.state = 49
            self.match(SampleParser.T__8)
            self.state = 50
            self.match(SampleParser.ID)
            self.state = 51
            self.match(SampleParser.T__9)
            self.state = 52
            self.assignment()
            self.state = 53
            self.match(SampleParser.T__7)
            self.state = 54
            self.condition()
            self.state = 55
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
            self.state = 57
            self.match(SampleParser.T__10)
            self.state = 58
            self.match(SampleParser.T__11)
            self.state = 59
            self.match(SampleParser.ID)
            self.state = 60
            self.match(SampleParser.T__12)
            self.state = 61
            self.columns()
            self.state = 62
            self.match(SampleParser.T__13)
            self.state = 63
            self.match(SampleParser.T__14)
            self.state = 64
            self.match(SampleParser.T__12)
            self.state = 65
            self.values()
            self.state = 66
            self.match(SampleParser.T__13)
            self.state = 67
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
        self.enterRule(localctx, 10, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SampleParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 70
                self.match(SampleParser.T__15)
                self.state = 71
                self.match(SampleParser.ID)
                self.state = 76
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
        self.enterRule(localctx, 12, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.value()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 78
                self.match(SampleParser.T__15)
                self.state = 79
                self.value()
                self.state = 84
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
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SampleParser.ID)
            self.state = 86
            self.match(SampleParser.T__16)
            self.state = 87
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
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(SampleParser.ID)
            self.state = 90
            self.comparator()
            self.state = 91
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
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==22 or _la==24):
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
        self.enterRule(localctx, 20, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4063232) != 0)):
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





