def freq_palavras(frase):
    '''função que recebe uma string e retorna um dicionário que diz a quantidade de 
    vezes que cada palavra apareceu na string dada
    string -> dicionario'''
    k = 0
    f = frase.split
    while k < len(f):
        l = list.count(f, f[k])
        l = dic[f[k]] 
        k = k + 1
    return dic