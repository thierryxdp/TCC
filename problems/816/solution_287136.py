def maiores(lista,inteiro_n):
    '''funcao que dada uma lista de numeros inteiros
    e um numero inteiro n, retorna outra lista
    que contenha todos os numeros da lista original
    maiores que n em ordem crescente'''
    
    
    lista2= []

    for i in lista:
      if i >inteiro_n:
        lista2.append(i)
    return lista2