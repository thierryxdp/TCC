def posLetra(frase, letra, ocorrencia):
    '''
Função que recebe uma string, uma letra e um numero n, retorna
o indice da n-esima ocorrencia da letra na string,
ou -1 caso nao haja esta ocorrencia.
str, str, int -> int
'''
    ind = -1
    for i in range(ocorrencia):
        ind = frase.find(letra, ind+1)
        if ind+1 > len(frase):
            return -1
    return ind