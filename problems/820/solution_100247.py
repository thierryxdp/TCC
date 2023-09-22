def posLetra(frase, letra, numero):
    '''função que conta quantas vezes uma letra apareceu
    em determinada ocorrência
    str, str, int--> int
    '''
    
    palavras = frase.split(' ')

    contador = 0
    ocorrencias = 0

    while len(palavras[numero - 1]) > contador:
        if letra in palavras[numero - 1]:
            ocorrencias += 1
            contador += 1

    if ocorrencias < numero:
        return -1
    else:
        return ocorrencias