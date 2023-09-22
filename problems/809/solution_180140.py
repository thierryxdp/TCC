def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída
    list,list -> list"""
    return lista1[0:1] + lista2[0:1] + lista1[0:lista1//2] + lista2[0:lista2//2] + lista1[-1:] + lista2[-1:]