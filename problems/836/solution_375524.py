import ast
def busca(setor,matriz):
    #str > list, str
    matriz = ast.literal_eval(matriz)
    for sublista in matriz:
            if setor in sublista[2]:
                return sublista
            else:
                return []