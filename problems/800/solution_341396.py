def total (lista, dicionario):
    '''recebe uma lista e um dicionario, calcula o valor total'''
    '''list, dict->int'''
    valor = []
    for itens in lista:
         if itens in dicionario:
            list.append(valor, dict.get (dicionario, itens))
    return round (sum(valor),2)