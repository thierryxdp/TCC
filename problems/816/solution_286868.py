def maiores (lista_de_numeros,numero):
    '''Dado uma lista de números inteiros e um número inteiro,
    a função deve retornar outra lista, com todos os números 
    da primeira lista maiores que n e ordenados em ordem 
    crescente;
    list, int -> list'''
    
    if numero in lista_de_numeros: 
        list.sort(lista_de_numeros)
        lista_de_numeros1=list.index(lista_de_numeros,numero)
        return lista_de_numeros[lista_de_numeros1+1:]
    
    else: 
        list.append(lista_de_numeros,numero)
        list.sort(lista_de_numeros)
        lista_de_numeros1=list.index(lista_de_numeros,numero)
        return lista_de_numeros[lista_de_numeros1+1:]