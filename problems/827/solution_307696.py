def qtd_divisores(numero):
    """FUNÇÃO QUE RETORNA A QUANTIDADE DE DIVISORES 
    DE UM NÚMERO
    INT=>INT"""
    divisores=0
    
    for i in range(1,numero+1):
        if numero%i==0:
            divisores+=1
    return divisores