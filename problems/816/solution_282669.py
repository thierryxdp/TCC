def maiores(lista_numero,n):
    '''Uma função dada uma lista de numeros inteiros e um numero inteiro n,
       e retorna outra lista, que contenha todos os numeros da lista original 
       maiores que n ordenados em ordem crescente. list[int],int -> list[int]'''
    numero = lista_numero
    numero.append(n)
    list.sort(lista_numero)
    if lista_numero[0] < n:
          return lista_numero = lista_numero.pop[0]
    elif lista_numero[1] < n:
        return lista_numero[1] = lista_numero.pop[1]