def posLetra(texto,letra,numero):
    '''Função que recebe uma string, uma letra e um número, que indica a ocorrência
desejada da letra. Retorna a posição na qual está a ocorrência da letra desejada,
caso exista menos ocorrências da letra do que a ocorrência pedida a função retornará: -1
'''
    lista = list()
    contador = 0
    if texto.count(letra)< numero:
        resposta = -1
    else:
        while contador <len(texto):
            if texto[contador] == letra:
                lista += [contador,]
            contador +=1
        resposta = lista [numero-1]
    return resposta