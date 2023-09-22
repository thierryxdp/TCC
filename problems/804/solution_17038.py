#Essa função filtra uma tupla com 4 elementos inteiros
#e retorna uma nova tupla somente com os números pares 
#na ordem que se encontravam.
# 'p' é a tupla com quatro elementos
# 't' é a nova tupla 
def filtra_pares (p):
    t=()
    if p[0]%2==0:
        t=t + (p[0],)
    if p[1]%2==0:
        t=t + (p[1],)
    if p[2]%2==0:
        t=t + (p[2],)
    if p[3]%2==0:
        t=t + (p[3],)
    return t