def posLetra(frase,letra,numero):
    '''Função que recebe como entrada uma string, uma letra, e um n ́umero que indica a
ocorrencia desejada da letra (1 para primeira ocorrencia, 2 para segunda, etc). Sua função retorna
em que posiçao da string aquela ocorrencia da letra esta.
	str,str,int-->int'''
    i = 0
    repeticoes = frase.count(letra)
    contador = 0
    if repeticoes<numero :
        return -1
    while i< len(frase):
        if letra in frase:
            contador = contador +1
        if contador == numero:
            posicao = frase.index(letra)
        i = i+1
    return posicao