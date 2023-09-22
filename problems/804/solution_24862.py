def filtra_pares(n):
    '''função que recebe ma tupla com quatro elementos inteiros como parâmetro, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam'''
    resultado=()
    if n[0]%2==0:
        resultado = resultado + (n[0],)
    if n[1]%2==0:
        resultado = resultado + (n[1],)
    if n[2]%2==0:
        resultado = resultado + (n[2],)
    if n[3]%2==0:
        resultado = resultado + (n[3],)
    return resultado