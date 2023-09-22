def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro,
    e retorna uma nova tupla contendo apenas os elementospares da tupla original,
    na mesma ordem em que se encontravam;
    tuple->tuple"""
    pares=()
    if (tupla[0]%2)==0:
        pares+=(tupla[0],)
    if (tupla[1]%2==0):
        pares+=(tupla[1],)
    if (tupla[2]%2==0):
        pares+=(tupla[2],)
    if (tupla[3]%2==0):
        pares+=(tupla[3],)
    return pares