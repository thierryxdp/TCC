def posLetra(frase,letra,numero):
    '''Função que recebe uma frase, uma letra e um numero de sequencia dessa letra, retornando a posição da letra indicada na frase
str,str,int -> int '''
    i = 0
    ocorrencias = 0
    if letra in frase:
        while i < len(frase):
            if frase[i] == letra:
                ocorrencias = ocorrencias + 1
            if ocorrencias == numero:
                return i
            i = i + 1
        return -1
    else:
        return 'Error: Letra não reconhecida na frase'