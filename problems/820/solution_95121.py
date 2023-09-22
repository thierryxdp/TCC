def posLetra(frase,letra,num):
    '''Escreva uma frase e uma letra. A funcao retorna a posicao da letra no
    texto em funcao da quantidade de aparicoes, contaveis atraves do num dado.
    ex: num=3 vai dar a posicao da letra dentro do texto na terceira aparicao da letra.
    Considere a primeira letra da frase como posicao 0, segunda letra posicao 1, e assim sucessivamente.
    Caso o num dado seja maior que as aparicoes, retorna -1
    str, str, int -> int'''
	contador=0
    i=0
    while i<len(frase):
        if frase[i]==letra:
            contador=contador+1
            if contador==num:
                return i
            i=i+1
        else:
            return -1