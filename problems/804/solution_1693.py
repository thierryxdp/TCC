def filtra_pares(x):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple(int,int,int,int)"""
    formato=()
    if x[0]%2==0:
        formato= formato + (x[0],)
    if x[1]%2==0:
        formato= formato + (x[1],)
    if x[2]%2==0:
        formato= formato + (x[2],)
    if x[3]%2==0:
        formato= formato + (x[3],)