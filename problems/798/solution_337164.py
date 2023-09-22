def freq_palavras(frases):
    '''função que, dada uma string qualquer, retorna
    um dicionário onde cada palavra da string é uma
    chave que tem como valor o número de vezes que 
    tal palavra aparece.
    str -> dic'''
    dic = {}
    lista = str.split(frases,' ')
    for x in lista:
        if x not in dic:
            dic[x] = 1
        if x in dic:
            dic[x] += 1
    return dic