def insere(lista_numero,n):
    '''funcao que ao receber uma lista composta por
    numeros inteiros na ordem crescente, insere 
    um numero n na devida posicao para que continue
    ordenada.
    list(int), int -> list(int)'''
    lista_mais_n = lista_numero + [n]
    list.sort(lista_mais_n)
    return lista_mais_n