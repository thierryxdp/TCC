def filtra_pares(tupla):
    """Função que recebe uma tupla com 4 elementos inteiros como
       parâmetro e retorna uma nova tupla contendo apenas os
       elementos pares da tupla original, na mesma ordem que se
       encontravam.
       int,int,int,int->tupla"""
    numerais = ()
    if tupla[0]%2 == 0:
        numerais = numerais + (tupla[0],)
    if tupla[1]%2 == 0:
        numerais = numerais + (tupla[1],)
    if tupla[2]%2 == 0:
        numerais = numerais + (tupla[2],)
    if tupla[3]%2 == 0:
        numerais = numerais + (tupla[3],)
        return numerais