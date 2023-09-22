def total(lista, preco):
    '''funcao que recebe uma lista de compras e um dicionario
       contendo o preco de cada produto, e retorna a soma 
       dos precos dos produtos que estao na lista de compras.
       list, dict -> float'''
    i = 0
    n_lista= []
    for x in range(len(lista)):
        if lista[i] in dict.keys(preco):
            list.append(n_lista, preco[lista[i]])
        i += 1
    return round(sum(n_lista), 2)