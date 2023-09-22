"""Recebe uma string, uma letra e um número que indica a ocorrência da letra,
retorna a posição da string da ocorrência indicada
str, str, int -> int"""

def posLetra(frase, letra, ocorrencia):
    i = 0
    o = 0
    pos = 0
    while i < len(frase):
        if frase[i] in letra:
            o = o + 1
            if o == ocorrencia:
                pos = i
                break
            elif ocorrencia > o:
                pos = -1
        i = i + 1
    return pos