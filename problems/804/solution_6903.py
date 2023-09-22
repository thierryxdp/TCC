def filtra_pares(tupla):
    """funcao que recebe uma tupla com quatro valores int e retorne uma nova tupla apenas com os valores pares da primeira tupla"""
    n=()
    if tupla[0]//2==0:
        n= n+(tupla[0],)
    if tupla[1]//2==0:
        n= n+(tupla[1],)
    if tupla[2]//2==0:
        n= n+(tupla[2],)
    if tupla[3]//2==0:
        n= n+(tupla[3],)
        return n