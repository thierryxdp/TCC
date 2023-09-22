def posLetra(frase,letra,num):
    '''Escreva uma frase e uma letra. A funcao conta quantas vezes
    a letra dada aparece na frase. Caso seja maior ou igual
    que o numero dado, retorna a ultimaa posicao em que a 
    letra se encontra; caso seja menor, retorna -1. Considere a primeira letra da frase
    como posicao 0, segunda letra posicao 1, e assim sucessivamente.
    str, str, int -> int'''
	contador=frase.count(letra)
    if contador>=num:
        return frase.rfind(letra)
    else:
        return -1