'''uma funcao que retorna apenas os valores maiores que a variavel de entrada n presente na lista
lista,int > lista'''

def maiores(lista, n):
    
    lista.append(n)
    lista.sort()
    index = lista.index(n)
    return lista[index+1:]