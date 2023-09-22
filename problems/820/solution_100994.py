def posLetra(frase, letra, ocorrencia):
    '''funcao que retorna a posicao que uma dada letra se encontra na frase de entrada, tendo
    em vista sua ocorrencia indicada. Caso a ocorrencia indicada seja menor que a quantidade da letra na frase, a funcao
    retornara -1.
    string, string, int -> int'''
    caracteres = 0
    qnt_letra = str.count(frase,letra)
    posicao = str.find(frase,letra)
    while caracteres<len(frase) and ocorrencia <= qnt_letra:
        posicao = posicao + str.find(frase,letra,caractere)
        caractere = caractere + 1
    return posicao