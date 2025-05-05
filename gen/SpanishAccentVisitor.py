# Generated from C:/Users/ghost/PycharmProjects/analizadorsintactico/SpanishAccent.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SpanishAccentParser import SpanishAccentParser
else:
    from SpanishAccentParser import SpanishAccentParser

# This class defines a complete generic visitor for a parse tree produced by SpanishAccentParser.

class SpanishAccentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpanishAccentParser#prog.
    def visitProg(self, ctx:SpanishAccentParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#sentence.
    def visitSentence(self, ctx:SpanishAccentParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#interrogative.
    def visitInterrogative(self, ctx:SpanishAccentParser.InterrogativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#exclamative.
    def visitExclamative(self, ctx:SpanishAccentParser.ExclamativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#declarative.
    def visitDeclarative(self, ctx:SpanishAccentParser.DeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#phrase.
    def visitPhrase(self, ctx:SpanishAccentParser.PhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#interrogative_word.
    def visitInterrogative_word(self, ctx:SpanishAccentParser.Interrogative_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpanishAccentParser#exclamative_word.
    def visitExclamative_word(self, ctx:SpanishAccentParser.Exclamative_wordContext):
        return self.visitChildren(ctx)



del SpanishAccentParser