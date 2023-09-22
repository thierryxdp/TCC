def filtra_pares(X):
    """Funcao que receba uma tupla com quatro elementos e retorna uma nova tupla par com os pares da tupla incial.
    tupla (int)->int"""
    Xf=()
    if X[0]%2 == 0:
        Xf = Xf + (X[0],)
    if X[1]%2 == 0:
        Xf = Xf + (X[1],)
    if X[2]%2 == 0:
        Xf = Xf + (X[2],)
    if X[3]%2 == 0:
        Xf = Xf + (X[3],)
    return Xf