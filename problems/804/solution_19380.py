def filtra_pares(p):
    '''função que ao receber uma tupla com 4 elementos inteiros, retorna uma nova tupla,contendo,apenas, os elementos pares da tupla recebida,na mesma ordem qem que foram inseridos; tuple -> tuple'''
    if p[0]%2==0:
        return p[0],
    if p[1]%2==0 and p[0]%2==0:
        return p[0],p[1]
    if p[2]%2==0 and p[1]%2==0 and p[0]%2==0:
        return p[0],p[1],p[2]
    if p[3]%2==0 and p[2]%2==0 and p[1]%2==0 and p[0]%2==0:
        return p[0],p[1],p[2],p[3]
    else:
        return ()