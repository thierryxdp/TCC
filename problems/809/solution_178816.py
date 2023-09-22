def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída
    list,list -> list"""
    L1 = [lista1]
    L2 = [lista2] 
    Lista = [lista1 + lista2]
    L3 = [Lista[0:1] + Lista[3:4] + Lista[1:2] + Lista[4:5] + Lista[2:3] + Lista[5:6]]
    return L3