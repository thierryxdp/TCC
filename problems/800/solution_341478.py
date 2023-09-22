def total(lista, dic):
    '''Função que calcula o valor da lista em relação ao dicionario
    list, dict--> float'''
    contador = 0
    valor = 0
    
    for produtos in lista:
        if lista[contador] in dic:
            valor += dic[lista[contador]]
            contador += 1
    return round(valor, 2)