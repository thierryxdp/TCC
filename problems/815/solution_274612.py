def insere(lista_numero,n):
    '''
    Dada uma lista crescente de números inteiros e um 
    número inteiro n, a função inclui n na posição
    correta, de tal maneira que a lista continue crescente. 
    list, int, list
    '''
    lista_numero.insert(0,n)
    return sorted(lista_numero)