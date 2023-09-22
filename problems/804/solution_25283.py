def par(n):
    'se um numero for par retorna true, se nao for retorna false. float->bool'
    n//2==0
def	filtra_pares(tupla):
    """recebe uma tupla com 4 elementos inteiros, e retorna uma nova tupla
    contendo apenas os elementos pares, na mesma ordem que estavam.tupla->tupla"""
    
    n1=tupla[0]
    n2=tupla[1]
    n3=tupla[2]
    n4=tupla[3]
    result=()
    
    if par(tupla[0]):
       result= result + (tupla[0],)
    if par(tupla[1]):
       result= result + (tupla[1],)
    if par(tupla[2]):
       result= result + (tupla[2],)
    if par(tupla[3]):
       result= result+(tupla[3],)
    return result