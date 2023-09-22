"""Recebe uma string, uma letra e um número que indica a ocorrência da letra,
retorna a posição da string da ocorrência indicada
str, str, int -> int"""

def posLetra(frase, letra, ocorrencia):
    i = 0
    o = 0
    while i < len(frase):
        if frase[i] in letra:
            o = o + 1
			if o == ocorrencia:
                pos = frase[i]
	return frase.index(pos)