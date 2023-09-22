def maiores(lista,n):
    '''funcao que dada uma lista de numeros inteiros e um numero inteiro n como parametros, retorna outra lista com os numeros 
      originais da lista de entrada ordenados em ordem crescentes que sejam maiores que n
      list,int->list'''
    list.insert(lista,0,n)
    list.sort(lista)
    s=str.partition(str(lista),n)
    a= str.join('',str.split(s))
    return list(a)