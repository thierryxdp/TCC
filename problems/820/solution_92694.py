def posLetra(frase,letra,numero):
    '''posLetra recebe uma frase, uma letra e um numero inteiro e devolve em que posição a ocorrencia da letra esta de acordo com o numero informado.
    Caso exista menos ocorrencias da letra do que a ocorrencia pedida a funcao deve retornar -1.
    str,str,int-->int'''
    if str.count(frase,letra)<numero:
        return -1
    else:
        i = 0
        ocorrencia = 0
        while ocorrencia<numero:
            if frase[i] == letra:
                ocorrencia = ocorrencia + 1
            i=i+1
        return i-1