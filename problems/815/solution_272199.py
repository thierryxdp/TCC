def insere(lista_numero,n):
    '''funcao que ao receber uma lista composta por
    numeros inteiros na ordem crescente, insere 
    um numero n na devida posicao para que continue
    ordenada.
    list(int), int -> list(int)'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero