import ast
def busca(setor,matriz):
    import ast
    #str > list, str
    matriz = ast.literal_eval(matriz)
    for sublista in matriz:
            if setor in sublista[2]:
                print(sublista)
            else:
                return []