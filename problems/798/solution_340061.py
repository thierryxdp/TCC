# frequencia de palavras
import re


def freq_palavras(frases):
    """Essa função recebe um texto e analisa a frequencia com que as palavras se repetem
    str -> dict"""
    freq = {}
    frases = frases.split()
    for i in range(len(frases)):
        if frases[i] in freq:
            freq[frases[i]] += 1
        if frases[i] not in freq:
            freq[frases[i]] = 1
    return freq