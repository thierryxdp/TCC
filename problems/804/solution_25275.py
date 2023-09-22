def par(n):
    'se um numero for par retorna true, se nao for retorna false. float->bool'
    n//2==0
def	filtra_pares(tupla):
    """recebe uma tupla com 4 elementos inteiros, e retorna uma nova tupla
    contendo apenas os elementos pares, na mesma ordem que estavam.tupla->tupla"""
    
    n1=tupla[0]
    result=()
    
    if par(n1):
       result= result + (n1,)
    if par(n2):
       result= result + (n2,)
    if par(n3):
       result= result + (n3,)
    if par(n4):
       result= result+(n4,)
    return result