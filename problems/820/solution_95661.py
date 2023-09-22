def posLetra(frase, letra, numero):
    '''Função que tem como entrada uma string, uma letra e um número indicando
    a ocorrência desejada da letra. Possui o retorno dizendo em qual posição da
    string aquela ocorrência da letra está.'''
    todas_aparicoes = str.count(frase, letra)
    busca = str.find(frase, letra) #busca da primeira vez que a letra aparece
    #no texto.
    contador = 1 #primeira aparição da letra na string.    
    if todas_aparicoes < numero:
        return -1
    while contador <= numero:
        posicao = str.find(frase, letra, busca)
        contador = contador + 1
        busca = posicao + 1
    return posicao