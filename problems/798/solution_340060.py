# frequencia de palavras
import re


def freq_palavras(texto):
    """Essa função recebe um texto e analisa a frequencia com que as palavras se repetem
    str -> dict"""
    freq = {}
    texto = texto.split()
    for i in range(len(texto)):
        if texto[i] in freq:
            freq[texto[i]] += 1
        if texto[i] not in freq:
            freq[texto[i]] = 1
    return freq