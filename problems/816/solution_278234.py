def maiores(lista, n):
    '''pega uma lista e compara com n so retorna os numeros maiores que n'''
    maior = []
    for i in lista:
        if i>n:
            maior.append(i)
    return(maior)