def filtra_pares(tupla):
    """função que recebe uma tupla de 4 inteiros e retorna uma nova tupla contendo apenas os elementos pares. tuple (int,int,int,int) -> tuple(int,int,int,int)"""
    resultado=()
    if tupla[0]%2==0:
        resultado = resultado+(tupla[0],)
    if tupla[1]%2==0:
        resultado = resultado+(tupla[1],)
    if tupla[2]%2==0:
        resultado = resultado+(tupla[2],)
    if tupla[3]%2==0:
        resultado = resultado+(tupla[3],)
return resultado