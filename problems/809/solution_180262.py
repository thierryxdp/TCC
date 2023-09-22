def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
res = lista1 + lista2
res[::] = lista1
res[1::2] = lista2
return list[res]