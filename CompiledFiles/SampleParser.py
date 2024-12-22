# Generated from Sample.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\3\6\7\6\62\n\6\f")
        buf.write("\6\16\6\65\13\6\5\6\67\n\6\3\6\3\6\3\6\2\4\4\6\7\2\4\6")
        buf.write("\b\n\2\4\3\2\6\7\3\2\b\t\2;\2\f\3\2\2\2\4\16\3\2\2\2\6")
        buf.write("\31\3\2\2\2\b*\3\2\2\2\n,\3\2\2\2\f\r\5\4\3\2\r\3\3\2")
        buf.write("\2\2\16\17\b\3\1\2\17\20\5\6\4\2\20\26\3\2\2\2\21\22\f")
        buf.write("\4\2\2\22\23\t\2\2\2\23\25\5\6\4\2\24\21\3\2\2\2\25\30")
        buf.write("\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\5\3\2\2\2\30\26")
        buf.write("\3\2\2\2\31\32\b\4\1\2\32\33\5\b\5\2\33!\3\2\2\2\34\35")
        buf.write("\f\4\2\2\35\36\t\3\2\2\36 \5\b\5\2\37\34\3\2\2\2 #\3\2")
        buf.write("\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2\2#!\3\2\2\2$+\5")
        buf.write("\n\6\2%&\7\3\2\2&\'\5\4\3\2\'(\7\4\2\2(+\3\2\2\2)+\7\13")
        buf.write("\2\2*$\3\2\2\2*%\3\2\2\2*)\3\2\2\2+\t\3\2\2\2,-\7\n\2")
        buf.write("\2-\66\7\3\2\2.\63\5\4\3\2/\60\7\5\2\2\60\62\5\4\3\2\61")
        buf.write("/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write("\67\3\2\2\2\65\63\3\2\2\2\66.\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("8\3\2\2\289\7\4\2\29\13\3\2\2\2\7\26!*\63\66")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Add", "Sub", "Mul", "Div", "Id", "Integer", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_funcCall = 4

    ruleNames =  [ "program", "expression", "term", "factor", "funcCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Add=4
    Sub=5
    Mul=6
    Div=7
    Id=8
    Integer=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(SampleParser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def Add(self):
            return self.getToken(SampleParser.Add, 0)

        def Sub(self):
            return self.getToken(SampleParser.Sub, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SampleParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SampleParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 15
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 16
                    _la = self._input.LA(1)
                    if not(_la==SampleParser.Add or _la==SampleParser.Sub):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 17
                    self.term(0) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(SampleParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(SampleParser.TermContext,0)


        def Mul(self):
            return self.getToken(SampleParser.Mul, 0)

        def Div(self):
            return self.getToken(SampleParser.Div, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SampleParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SampleParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 26
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 27
                    _la = self._input.LA(1)
                    if not(_la==SampleParser.Mul or _la==SampleParser.Div):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 28
                    self.factor() 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(SampleParser.FuncCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(SampleParser.ExpressionContext,0)


        def Integer(self):
            return self.getToken(SampleParser.Integer, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = SampleParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampleParser.Id]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.funcCall()
                pass
            elif token in [SampleParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(SampleParser.T__0)
                self.state = 36
                self.expression(0)
                self.state = 37
                self.match(SampleParser.T__1)
                pass
            elif token in [SampleParser.Integer]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(SampleParser.Integer)
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


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(SampleParser.Id, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SampleParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = SampleParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SampleParser.Id)
            self.state = 43
            self.match(SampleParser.T__0)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.T__0) | (1 << SampleParser.Id) | (1 << SampleParser.Integer))) != 0):
                self.state = 44
                self.expression(0)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SampleParser.T__2:
                    self.state = 45
                    self.match(SampleParser.T__2)
                    self.state = 46
                    self.expression(0)
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 54
            self.match(SampleParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




