def filtra_pares(tupla):
    """Função que recebe uma tupla com 4 elementos inteiros como
       parâmetro e retorna uma nova tupla contendo apenas os
       elementos pares da tupla original, na mesma ordem que se
       encontravam.
       int,int,int,int->tupla"""
    numerais = ()
    if numeros[0]%2 == 0:
        numerais = numerais + (numeros[0],)
    if numeros[1]%2 == 0:
        numerais = numerais + (numeros[1],)
    if numeros[2]%2 == 0:
        numerais = numerais + (numeros[2],)
    if numeros[3]%2 == 0:
        numerais = numerais + (numeros[3],)
        return numerais