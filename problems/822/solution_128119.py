def repetidos(lista):
    '''Dada uma lista de numeros, retorna a quantidade de vezes que os números
se repetem em sequencia.
list -> int'''
    i=0
    resultado=0
    for n in range(0,len(lista)):
        if lista[n] == lista[n-1]:
            resultado += 1
    return resultado