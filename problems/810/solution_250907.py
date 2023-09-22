""" A função ira renomear "-" "," "." "!" "?" para "/" e
depois ira renomeala para uma string vazia, a função ira separar a string e
e depois inverte a sua ordem e usando o comando "join" ela ira juntar novamente a
string

str --> str"""
def inverte(x):
    X = str.lower(x)
    A = X.replace("-"," ")
    B = A.replace(",","/")
    C = B.replace(".","/")
    D = C.replace("!","/")
    E = D.replace("?","/")
    F = E.replace("/","")
    G = F.split()
    H = G[::-1]
    I = str.join(" ",H)
    return I