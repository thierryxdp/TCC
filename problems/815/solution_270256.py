def insere(lista_numero,n):
    '''comentario'''
    lista_numero = []
    for x in range(8):
        n = int(input("Digite um numero inteiro:"))
        lista_numero.append(n)
        lista_numero.sort()
        print(lista_numero)