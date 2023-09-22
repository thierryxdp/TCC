def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    
    lista1 = [1,3,5]
    lista2 = [2,4,6]
    lista3 = []
    lista3 = lista1 + lista2
    lista3[:2] = lista1
    lista3[2:] = lista2
       return lista3