# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:12:44 2022

@author: Oguhan DUYAR (oguzhan.duyar.ogresyus@gmail.com)
"""
# Protein Dictionary
proteincode = {  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T',
             'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S',
             'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P',
             'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
             'CGA':'R', 'CGC':'R','CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V',
             'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D',
             'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S',
             'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
             'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*','TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}


def gentocod(genstr):
    codon=[]
    for x in range(0, len(genstr), 3):
        y=genstr[x:x+3]
        codon.append(y)
    return codon
        


# def codtopro(codstr):