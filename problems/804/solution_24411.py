def filtra_pares(x):
    '''Função receba uma tupla com quatro elementos inteiros como parâmetro,
    e retorne uma nova tupla contendo apenas os elementos pares da tupla original;
    tupla->tupla'''
    lista = ()
    if x[0]%2==0:
        lista=lista+(x[0],)
    if x[1]%2==0:
        lista=lista+(x[1],)
    if x[2]%2==0:
        lista=lista+(x[2],)
    if x[3]%2==0:
        lista=lista+(x[3],)
    return lista