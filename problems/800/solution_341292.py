def total(lista,dicionario):
    '''função que recebe uma lista de compras e um dicionario com os produtos e os seus respectivos valores e retorna a soma dos valores dos produtos(com duas casas decimais) que estão tanto na lista quanto no dicionariolist,dicr->int'''
    soma=0
    for i in lista:
        if i in dict.keys(dicionario):
            soma=soma+dicionario[i]
    return round(soma,2)