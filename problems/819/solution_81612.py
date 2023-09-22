# Função que filtra os múltilpos
# n é uma lista de números 
def filtraMultiplos(listanumero,n):
    """Função que filtra os múltiplos de uma lista n, sendo o número "filtrador" n"""
    """Parâmetros de entrada:list, float"""
    """Parâmetros de saída:list"""
    multiplos=[]
    proximo=0
    while proximo<len(listanumero):
        if listanumero[proximo]%n==0:
            multiplos+=listanumero[proximo]
            proximo+=1
    return multiplos