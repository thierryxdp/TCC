def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario tais que as chaves sao as palavras dessa string e tenham como chaves associadas o valor do numero de vezes que a palavra aparece na string
str -> dict'''
    lista = str.split(frases)
    dicionario={}
    for i in range(len(lista)):
        repeticoes=list.count(lista,i))
        if lista[i] not in dicionario:
            dicionario[i]=repeticoes
    return dicionario