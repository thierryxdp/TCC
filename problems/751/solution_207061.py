'''Função que recebe uma frase e retorna quantas palavras ela contém.
	A frase deve, obrigatoriamente, ser inserida entre aspas.
    str -> int'''
def quant_palavras(frase):
    return len(frase.split(' '))