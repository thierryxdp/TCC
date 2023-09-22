# Função que filtra os múltilpos
# n é uma lista de números 
def filtraMultiplos(lista_numero,n):
    """Função que filtra os múltiplos de uma lista n, sendo o número "filtrador" n"""
    """Parâmetros de entrada:list, float"""
    """Parâmetros de saída:list"""
    acumulador=[]
    contador=0
    while contador<len(lista_numero):
        if lista_numero[contador]%n==0:
            acumulador+=[lista_numero[contador]]
        contador+=1
    return acumulador