def inserir(lista_numero,n):
    '''Uma lista crescente de numeros inteiros e um outro numero
    inteiro n, cria-se uma função na qual ao inserir n na lista
    a mesma continue crescente'''
    lista_numero.insert(0,n)
    return sorted(lista_numero)