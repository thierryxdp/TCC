'''uma funcao que retorna uma lista com a variavel n inserida e ordenada de forma crescente
lista, int > lista'''

def insere(lista_numero, n):
    
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero