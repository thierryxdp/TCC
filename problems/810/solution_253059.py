""" A função ira renomear "-" "," "." "!" "?" para  renomeala para uma string vazia, 
a função ira separar a string e depois inverte a sua ordem, usando o comando "join" ela ira juntar novamente a
string

str --> str"""
def inverte(x):
    X = str.lower(x)
    A = X.replace("-"," ")
    B = A.replace(",","")
    C = B.replace(".","")
    D = C.replace("!","")
    E = D.replace("?","")
    F = E.split()
    G = F[::-1]
    H = str.join(" ",G)
    return H