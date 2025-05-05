# Generated from C:/Users/ghost/PycharmProjects/analizadorsintactico/SpanishAccent.g4 by ANTLR 4.13.2
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
        4,1,13,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,1,1,3,
        1,28,8,1,1,1,3,1,31,8,1,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,37,1,2,
        1,2,1,3,1,3,1,3,4,3,45,8,3,11,3,12,3,46,1,3,1,3,1,4,1,4,4,4,53,8,
        4,11,4,12,4,54,1,5,1,5,5,5,59,8,5,10,5,12,5,62,9,5,1,6,1,6,1,7,1,
        7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,12,13,1,0,1,6,68,0,18,1,0,
        0,0,2,27,1,0,0,0,4,32,1,0,0,0,6,41,1,0,0,0,8,50,1,0,0,0,10,56,1,
        0,0,0,12,63,1,0,0,0,14,65,1,0,0,0,16,19,3,2,1,0,17,19,3,10,5,0,18,
        16,1,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,
        0,21,22,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,28,3,4,2,0,25,28,3,
        6,3,0,26,28,3,8,4,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,
        30,1,0,0,0,29,31,5,11,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,
        0,32,33,5,7,0,0,33,35,3,12,6,0,34,36,7,0,0,0,35,34,1,0,0,0,36,37,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,8,0,0,
        40,5,1,0,0,0,41,42,5,9,0,0,42,44,3,14,7,0,43,45,7,0,0,0,44,43,1,
        0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,
        49,5,10,0,0,49,7,1,0,0,0,50,52,5,12,0,0,51,53,7,0,0,0,52,51,1,0,
        0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,60,
        5,12,0,0,57,59,7,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,
        60,61,1,0,0,0,61,11,1,0,0,0,62,60,1,0,0,0,63,64,7,1,0,0,64,13,1,
        0,0,0,65,66,7,1,0,0,66,15,1,0,0,0,8,18,20,27,30,37,46,54,60
    ]

class SpanishAccentParser ( Parser ):

    grammarFileName = "SpanishAccent.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\u00BF'", 
                     "'?'", "'\\u00A1'", "'!'" ]

    symbolicNames = [ "<INVALID>", "QUE", "COMO", "CUANDO", "DONDE", "QUIEN", 
                      "CUANTO", "INTERROG_OPEN", "INTERROG_CLOSE", "EXCLAM_OPEN", 
                      "EXCLAM_CLOSE", "PUNCT_END", "ANY_WORD", "WS" ]

    RULE_prog = 0
    RULE_sentence = 1
    RULE_interrogative = 2
    RULE_exclamative = 3
    RULE_declarative = 4
    RULE_phrase = 5
    RULE_interrogative_word = 6
    RULE_exclamative_word = 7

    ruleNames =  [ "prog", "sentence", "interrogative", "exclamative", "declarative", 
                   "phrase", "interrogative_word", "exclamative_word" ]

    EOF = Token.EOF
    QUE=1
    COMO=2
    CUANDO=3
    DONDE=4
    QUIEN=5
    CUANTO=6
    INTERROG_OPEN=7
    INTERROG_CLOSE=8
    EXCLAM_OPEN=9
    EXCLAM_CLOSE=10
    PUNCT_END=11
    ANY_WORD=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SpanishAccentParser.EOF, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpanishAccentParser.SentenceContext)
            else:
                return self.getTypedRuleContext(SpanishAccentParser.SentenceContext,i)


        def phrase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpanishAccentParser.PhraseContext)
            else:
                return self.getTypedRuleContext(SpanishAccentParser.PhraseContext,i)


        def getRuleIndex(self):
            return SpanishAccentParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SpanishAccentParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.sentence()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.phrase()
                    pass


                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4736) != 0)):
                    break

            self.state = 22
            self.match(SpanishAccentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interrogative(self):
            return self.getTypedRuleContext(SpanishAccentParser.InterrogativeContext,0)


        def exclamative(self):
            return self.getTypedRuleContext(SpanishAccentParser.ExclamativeContext,0)


        def declarative(self):
            return self.getTypedRuleContext(SpanishAccentParser.DeclarativeContext,0)


        def PUNCT_END(self):
            return self.getToken(SpanishAccentParser.PUNCT_END, 0)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = SpanishAccentParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 24
                self.interrogative()
                pass
            elif token in [9]:
                self.state = 25
                self.exclamative()
                pass
            elif token in [12]:
                self.state = 26
                self.declarative()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 29
                self.match(SpanishAccentParser.PUNCT_END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterrogativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERROG_OPEN(self):
            return self.getToken(SpanishAccentParser.INTERROG_OPEN, 0)

        def interrogative_word(self):
            return self.getTypedRuleContext(SpanishAccentParser.Interrogative_wordContext,0)


        def INTERROG_CLOSE(self):
            return self.getToken(SpanishAccentParser.INTERROG_CLOSE, 0)

        def ANY_WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.ANY_WORD)
            else:
                return self.getToken(SpanishAccentParser.ANY_WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.WS)
            else:
                return self.getToken(SpanishAccentParser.WS, i)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_interrogative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterrogative" ):
                listener.enterInterrogative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterrogative" ):
                listener.exitInterrogative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterrogative" ):
                return visitor.visitInterrogative(self)
            else:
                return visitor.visitChildren(self)




    def interrogative(self):

        localctx = SpanishAccentParser.InterrogativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_interrogative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SpanishAccentParser.INTERROG_OPEN)
            self.state = 33
            self.interrogative_word()
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12 or _la==13):
                    break

            self.state = 39
            self.match(SpanishAccentParser.INTERROG_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExclamativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAM_OPEN(self):
            return self.getToken(SpanishAccentParser.EXCLAM_OPEN, 0)

        def exclamative_word(self):
            return self.getTypedRuleContext(SpanishAccentParser.Exclamative_wordContext,0)


        def EXCLAM_CLOSE(self):
            return self.getToken(SpanishAccentParser.EXCLAM_CLOSE, 0)

        def ANY_WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.ANY_WORD)
            else:
                return self.getToken(SpanishAccentParser.ANY_WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.WS)
            else:
                return self.getToken(SpanishAccentParser.WS, i)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_exclamative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclamative" ):
                listener.enterExclamative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclamative" ):
                listener.exitExclamative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExclamative" ):
                return visitor.visitExclamative(self)
            else:
                return visitor.visitChildren(self)




    def exclamative(self):

        localctx = SpanishAccentParser.ExclamativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exclamative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SpanishAccentParser.EXCLAM_OPEN)
            self.state = 42
            self.exclamative_word()
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12 or _la==13):
                    break

            self.state = 48
            self.match(SpanishAccentParser.EXCLAM_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.ANY_WORD)
            else:
                return self.getToken(SpanishAccentParser.ANY_WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.WS)
            else:
                return self.getToken(SpanishAccentParser.WS, i)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_declarative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarative" ):
                listener.enterDeclarative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarative" ):
                listener.exitDeclarative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarative" ):
                return visitor.visitDeclarative(self)
            else:
                return visitor.visitChildren(self)




    def declarative(self):

        localctx = SpanishAccentParser.DeclarativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declarative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SpanishAccentParser.ANY_WORD)
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 51
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.ANY_WORD)
            else:
                return self.getToken(SpanishAccentParser.ANY_WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SpanishAccentParser.WS)
            else:
                return self.getToken(SpanishAccentParser.WS, i)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhrase" ):
                return visitor.visitPhrase(self)
            else:
                return visitor.visitChildren(self)




    def phrase(self):

        localctx = SpanishAccentParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SpanishAccentParser.ANY_WORD)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interrogative_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUE(self):
            return self.getToken(SpanishAccentParser.QUE, 0)

        def COMO(self):
            return self.getToken(SpanishAccentParser.COMO, 0)

        def CUANDO(self):
            return self.getToken(SpanishAccentParser.CUANDO, 0)

        def DONDE(self):
            return self.getToken(SpanishAccentParser.DONDE, 0)

        def QUIEN(self):
            return self.getToken(SpanishAccentParser.QUIEN, 0)

        def CUANTO(self):
            return self.getToken(SpanishAccentParser.CUANTO, 0)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_interrogative_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterrogative_word" ):
                listener.enterInterrogative_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterrogative_word" ):
                listener.exitInterrogative_word(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterrogative_word" ):
                return visitor.visitInterrogative_word(self)
            else:
                return visitor.visitChildren(self)




    def interrogative_word(self):

        localctx = SpanishAccentParser.Interrogative_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_interrogative_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
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


    class Exclamative_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUE(self):
            return self.getToken(SpanishAccentParser.QUE, 0)

        def COMO(self):
            return self.getToken(SpanishAccentParser.COMO, 0)

        def CUANDO(self):
            return self.getToken(SpanishAccentParser.CUANDO, 0)

        def DONDE(self):
            return self.getToken(SpanishAccentParser.DONDE, 0)

        def QUIEN(self):
            return self.getToken(SpanishAccentParser.QUIEN, 0)

        def CUANTO(self):
            return self.getToken(SpanishAccentParser.CUANTO, 0)

        def getRuleIndex(self):
            return SpanishAccentParser.RULE_exclamative_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclamative_word" ):
                listener.enterExclamative_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclamative_word" ):
                listener.exitExclamative_word(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExclamative_word" ):
                return visitor.visitExclamative_word(self)
            else:
                return visitor.visitChildren(self)




    def exclamative_word(self):

        localctx = SpanishAccentParser.Exclamative_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exclamative_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
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





