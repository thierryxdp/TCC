def insere(lista_numero,n):
    '''Adiciona um numero (n) na posição correta a uma lista
       ordenada de forma crescente e retorna a lista alterada;
       list, int -> list'''
    
    lista = lista_numero
    lista.append(n)
    
    return lista.sort()