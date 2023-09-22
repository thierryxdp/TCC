def freq_palavras(frases):
    '''recebe uma str e retorna um dicionario com cada palavra como key e a qtd de 
    vezes que ela aparece como valor'''
    lista = (str.split(frases, ' '))
    dicionario = {}
    for i in lista:
        dicionario.setdefault(i, list.count(lista, i))
    
    return dicionario