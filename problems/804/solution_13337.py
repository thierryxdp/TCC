"""analisamos a tupla fornecida, conferindo se o resto da divisao por 2
iguala a zero, para saber se o numero respectivo e par, e adicionamos a 
nova tupla
tupla->tupla"""
def filtra_pares(a):
    q=()
    if a[0]%2==0:
        q=q+(a[0],)
    if a[1]%2==0:
        q=q+(a[1],)
    if a[2]%2==0:
        q=q+(a[2],)
    if a[3]%2==0:
        q=q+(a[3],)
    return q