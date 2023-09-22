def insere(lista_numero,n):
    '''comentario'''
    lista = []
    for x in range(8):
        n = int(input("Digite um numero inteiro:"))
        lista.append(n)
        lista.sort()
        print(lista)