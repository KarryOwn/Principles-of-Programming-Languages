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
        4,1,20,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,56,8,4,10,4,
        12,4,59,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,
        0,0,9,0,2,4,6,8,10,12,14,16,0,2,2,0,17,17,19,19,1,0,12,16,68,0,19,
        1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,44,1,0,0,0,8,52,1,0,0,0,10,60,
        1,0,0,0,12,64,1,0,0,0,14,68,1,0,0,0,16,70,1,0,0,0,18,20,3,2,1,0,
        19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,
        0,0,23,35,3,4,2,0,24,35,3,6,3,0,25,26,5,1,0,0,26,27,5,2,0,0,27,28,
        5,17,0,0,28,29,5,3,0,0,29,30,5,18,0,0,30,35,5,4,0,0,31,32,5,5,0,
        0,32,33,5,18,0,0,33,35,5,4,0,0,34,23,1,0,0,0,34,24,1,0,0,0,34,25,
        1,0,0,0,34,31,1,0,0,0,35,3,1,0,0,0,36,37,5,6,0,0,37,38,3,8,4,0,38,
        39,5,7,0,0,39,40,5,18,0,0,40,41,5,8,0,0,41,42,3,12,6,0,42,43,5,4,
        0,0,43,5,1,0,0,0,44,45,5,9,0,0,45,46,5,18,0,0,46,47,5,10,0,0,47,
        48,3,10,5,0,48,49,5,8,0,0,49,50,3,12,6,0,50,51,5,4,0,0,51,7,1,0,
        0,0,52,57,5,18,0,0,53,54,5,11,0,0,54,56,5,18,0,0,55,53,1,0,0,0,56,
        59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,9,1,0,0,0,59,57,1,0,0,
        0,60,61,5,18,0,0,61,62,5,12,0,0,62,63,3,14,7,0,63,11,1,0,0,0,64,
        65,5,18,0,0,65,66,3,16,8,0,66,67,3,14,7,0,67,13,1,0,0,0,68,69,7,
        0,0,0,69,15,1,0,0,0,70,71,7,1,0,0,71,17,1,0,0,0,3,21,34,57
    ]

class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'from'", "'as'", "';'", "'display'", 
                     "'SELECT'", "'FROM'", "'WHERE'", "'UPDATE'", "'SET'", 
                     "','", "'='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "ID", "INTEGER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_updateStmt = 3
    RULE_columns = 4
    RULE_assignment = 5
    RULE_condition = 6
    RULE_value = 7
    RULE_comparator = 8

    ruleNames =  [ "program", "statement", "selectStmt", "updateStmt", "columns", 
                   "assignment", "condition", "value", "comparator" ]

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
    STRING=17
    ID=18
    INTEGER=19
    WS=20

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 610) != 0)):
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.selectStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.updateStmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(SampleParser.T__0)
                self.state = 26
                self.match(SampleParser.T__1)
                self.state = 27
                self.match(SampleParser.STRING)
                self.state = 28
                self.match(SampleParser.T__2)
                self.state = 29
                self.match(SampleParser.ID)
                self.state = 30
                self.match(SampleParser.T__3)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(SampleParser.T__4)
                self.state = 32
                self.match(SampleParser.ID)
                self.state = 33
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
            self.state = 36
            self.match(SampleParser.T__5)
            self.state = 37
            self.columns()
            self.state = 38
            self.match(SampleParser.T__6)
            self.state = 39
            self.match(SampleParser.ID)
            self.state = 40
            self.match(SampleParser.T__7)
            self.state = 41
            self.condition()
            self.state = 42
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
            self.state = 44
            self.match(SampleParser.T__8)
            self.state = 45
            self.match(SampleParser.ID)
            self.state = 46
            self.match(SampleParser.T__9)
            self.state = 47
            self.assignment()
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
        self.enterRule(localctx, 8, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SampleParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 53
                self.match(SampleParser.T__10)
                self.state = 54
                self.match(SampleParser.ID)
                self.state = 59
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
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SampleParser.ID)
            self.state = 61
            self.match(SampleParser.T__11)
            self.state = 62
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
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(SampleParser.ID)
            self.state = 65
            self.comparator()
            self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==17 or _la==19):
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
        self.enterRule(localctx, 16, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
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





