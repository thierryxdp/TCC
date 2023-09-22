def filtra_pares(tupla):
    """função que recebe uma tupla com quatro valores int e retorne uma nova tupla apenas com os valores pares da primeira tupla"""
    x=()
    if tupla[0]%2==0:
        x= x+(tupla[0],)
    if tupla[1]%2==0:
        x= x+(tupla[1],)
    if tupla[2]%2==0:
        x= x+(tupla[2],)
    if tupla[3]%2==0:
        x= x+(tupla[3],)
        return x