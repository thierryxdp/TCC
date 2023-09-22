def posLetra(frase, letra, ocorrencia):
    '''funcao que retorna a posicao que uma dada letra se encontra na frase de entrada, tendo
    em vista sua ocorrencia indicada. Caso a ocorrencia indicada seja menor que a quantidade da letra na frase, a funcao
    retornara -1.
    string, string, int -> int'''
    qnt_letra = str.count(frase,letra)
    posicao = str.find(frase,letra)
    while ocorrencia <= qnt_letra:
        posicao = str.find(frase,letra,posicao + 1)
        ocorrencia = ocorrencia + 1
 
    return posicao