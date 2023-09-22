def posLetra(frase, letra, ocorrencia):
    '''funcao que retorna a posicao que uma dada letra se encontra na frase de entrada, tendo
    em vista sua ocorrencia indicada. Caso a ocorrencia indicada seja menor que a quantidade da letra na frase, a funcao
    retornara -1.
    string, string, int -> int'''
    i = 0
    posicao = 0
    if ocorrencia > str.count(frase,letra):
            return -1
    while i<len(frase):
        posicao=str.find(frase,letra,posicao)
        posicao = posicao + 1
        i=i+1
    return posicao