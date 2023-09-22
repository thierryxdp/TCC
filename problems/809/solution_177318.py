def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista3 = list()
    for a,b in zip(lista1,lista2):
        lista3.append(a)
        lista3.append(b)
        return lista3
    print(f'/n números da lista 1, antes de serem intercalados:{lista1}')
    print(f'/n números da lista 2, antes de serem intercalados:{lista2}')
    print(f'/n números da lista 3, com números intercala: n {intercala(lista1,lista2)}')