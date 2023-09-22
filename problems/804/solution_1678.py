def filtra_pares(x):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple"""
    if x[0]%2==0:
        formato1= x[0]
    else:
        formato1=()
    if x[1]%2==0:
        formato2= x[1]
    else:
        formato2=()
    if x[2]%2==0:
        formato3=x[2]
    else:
        formato3=()
    if x[3]%2==0:
        formato4= x[3]
    else:
        formato4= ()
        
formatosPossiveis= formato1+formato2+formato3+formato4
    
    return formatosPossiveis