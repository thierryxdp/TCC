def insere(lista_numero,n):
    '''comentario'''
    lista_numero = []
    in range(8):
        n = int(input("Digite um numero inteiro:"))
        lista_numero.append(n)
        lista_numero.sort()
        print(lista_numero)