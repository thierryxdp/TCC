def soma(mat):
    c = 0
    for lin in mat:
        for e in lin:
            c = c + e
    return c

def n_elementos(mat):
    c = 0
    for lin in mat:
        for col in lin:
            c = c + 1
    return c

def media_matriz(mat):
    return round(soma(mat)/n_elementos(mat),2)