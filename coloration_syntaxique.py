#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
# Python 2.7

import os, sys

from PyQt4 import QtCore, QtGui


#############################################################################
class ColorSyntaxSQL(QtGui.QSyntaxHighlighter):
    # ========================================================================
    def __init__(self, parent=None):
        super(ColorSyntaxSQL, self).__init__(parent)

        # liste des règles: [[regex, format], [regex, format], ...]
        self.regles = []

        # --------------------------------------------------------------------
        # FORMAT DES CODES G
        motcles_codeG_format = QtGui.QTextCharFormat()
        motcles_codeG_format.setForeground(QtCore.Qt.blue)  # mots clés en bleu
        motcles_codeG_format.setFontWeight(QtGui.QFont.Bold)  # pour mise en gras

        motcles_fonctionM_format = QtGui.QTextCharFormat()
        motcles_fonctionM_format.setForeground(QtCore.Qt.red)  # mots clés en bleu
        motcles_fonctionM_format.setFontWeight(QtGui.QFont.Bold)  # pour mise en gras

        motcles_structure_format = QtGui.QTextCharFormat()
        motcles_structure_format.setForeground(QtCore.Qt.black)  # mots clés en bleu
        motcles_structure_format.setFontWeight(QtGui.QFont.Bold)  # pour mise en gras

        motcles_origine_format = QtGui.QTextCharFormat()
        motcles_origine_format.setForeground(QtCore.Qt.darkYellow)  # mots clés en bleu
        motcles_origine_format.setFontWeight(QtGui.QFont.Bold)  # pour mise en gras

        motcles_XYZ_format = QtGui.QTextCharFormat()
        motcles_XYZ_format.setForeground(QtCore.Qt.black)  # mots clés en bleu
        motcles_XYZ_format.setFontWeight(QtGui.QFont.Bold)  # pour mise en gras

        # LES CODES G
        motcles_codeG = ["G0", "G1", "G2", "G3", "G9", "G10", "G12", "G16", "G17", "G18", "G19", "G31", "G40",
                         "G41", "G42", "G45", "G51", "G52", "G53", "G70", "G71", "G73", "G74", "G75", "G76",
                         "G77", "G79", "G80", "G81", "G82", "G83", "G84", "G85", "G86", "G87", "G88", "G89",
                          "G90", "G91", "G92", "G93", "G94"]

        #APPLICATION FORMAT CODE G
        for motcles_codeG in motcles_codeG:
            motcles_regex = QtCore.QRegExp("\\b" + motcles_codeG + "\\b", QtCore.Qt.CaseInsensitive)
            self.regles.append([motcles_regex, motcles_codeG_format])


        #LES FONCTIONS M
        motcles_fonctionM = ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M19", "M40",
                             "M41", "M42", "M43", "M44", "M45", "M48", "M49", "M64", "M65",
                             "M66", "M67", "M31", "M17", "M52", "M1", "M1"]

        #APPLICATION FORMAT FONCTION M
        for motcles_fonctionM in motcles_fonctionM:
            motcles_regex = QtCore.QRegExp("\\b" + motcles_fonctionM + "\\b", QtCore.Qt.CaseInsensitive)
            self.regles.append([motcles_regex, motcles_fonctionM_format])

        #LES STRUCTURES DE CODE
        motcles_structure = ["IF", "ELSE", "ENDIF", "LOOP", "ENDLOOP", "FOR", "TO", "ENDFOR", "DEF", "SET", "REP", "TRUNC", "MINVAL", "MAXVAL",
                             "BOUND", "STRING", "NUMBER", "ISNUMBER", "AXNAME", "TOLOWER", "TOUPPER", "STRLEN", "GOTOB",
                             "GOTOF", "GOTO", "GOTOC", "CASE", "OF", "DEFAULT", "REPEAT", "REPEATB", "ENDLABEL", "WHILE", "ENDWHILE",
                             "REPEAT", "UNTIL", "INIT", "START", "WAITM", "WAITMC", "MSG"]

        #APPLICATION FORMAT STRUCTURE
        for motcles_structure in motcles_structure:
            motcles_regex = QtCore.QRegExp("\\b" + motcles_structure + "\\b", QtCore.Qt.CaseInsensitive)
            self.regles.append([motcles_regex, motcles_structure_format])

        #LES DECALAGES D ORIGINES
        motcles_origine = ["G54", "G55", "G56", "G57", "G58", "G59", "G501", "G502"]


        # APPLICATION FORMAT FONCTION M
        for motcles_origine in motcles_origine:
            motcles_regex = QtCore.QRegExp("\\b" + motcles_origine + "\\b", QtCore.Qt.CaseInsensitive)
            self.regles.append([motcles_regex, motcles_origine_format])



        # --------------------------------------------------------------------
        # nombre entier ou flottant
        nombre_format = QtGui.QTextCharFormat()
        nombre_format.setForeground(QtCore.Qt.darkGreen)
        nombre_motif = "\\b[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?\\b"
        nombre_regex = QtCore.QRegExp(nombre_motif)
        nombre_regex.setMinimal(True)
        self.regles.append([nombre_regex, nombre_format])

        # --------------------------------------------------------------------
        # chaine de caractères simple quote: '...'
        chaine1_format = QtGui.QTextCharFormat()
        chaine1_format.setForeground(QtCore.Qt.green)  # red)
        chaine1_motif = "\'.*\'"
        chaine1_regex = QtCore.QRegExp(chaine1_motif)
        chaine1_regex.setMinimal(True)
        self.regles.append([chaine1_regex, chaine1_format])

        # --------------------------------------------------------------------
        # chaine de caractères double quotes: "..."
        chaine2_format = QtGui.QTextCharFormat()
        chaine2_format.setForeground(QtCore.Qt.red)
        chaine2_motif = '\".*\"'
        chaine2_regex = QtCore.QRegExp(chaine2_motif)
        chaine2_regex.setMinimal(True)
        self.regles.append([chaine2_regex, chaine2_format])

        # --------------------------------------------------------------------
        # delimiteur: parenthèses, crochets, accolades
        delimiteur_format = QtGui.QTextCharFormat()
        delimiteur_format.setForeground(QtCore.Qt.darkGray)
        delimiteur_format.setFontWeight(QtGui.QFont.Bold)
        delimiteur_motif = "[\)\(]+|[\{\}]+|[][]+|[\XYZAB]"
        delimiteur_regex = QtCore.QRegExp(delimiteur_motif)
        self.regles.append([delimiteur_regex, delimiteur_format])

        # --------------------------------------------------------------------
        # commentaire sur une seule ligne et jusqu'à fin de ligne: ;...\n
        comment_format = QtGui.QTextCharFormat()
        comment_format.setForeground(QtCore.Qt.gray)
        comment_motif = ";[^\n]*"
        comment_regex = QtCore.QRegExp(comment_motif)
        self.regles.append([comment_regex, comment_format])

        # --------------------------------------------------------------------
        # commentaires multi-lignes: /*...*/
        self.commentml_format = QtGui.QTextCharFormat()
        self.commentml_format.setForeground(QtCore.Qt.gray)

        self.commentml_deb_regex = QtCore.QRegExp("/\\*")
        self.commentml_fin_regex = QtCore.QRegExp("\\*/")

    # ========================================================================
    def highlightBlock(self, text):
        """analyse chaque ligne et applique les règles"""

        # analyse des lignes avec les règles
        for expression, tformat in self.regles:
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, tformat)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # pour les commentaires multilignes: /* ... */
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentml_deb_regex.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentml_fin_regex.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentml_lg = len(text) - startIndex
            else:
                commentml_lg = endIndex - startIndex + \
                               self.commentml_fin_regex.matchedLength()

            self.setFormat(startIndex, commentml_lg, self.commentml_format)

            startIndex = self.commentml_deb_regex.indexIn(text,
                                                          startIndex + commentml_lg)