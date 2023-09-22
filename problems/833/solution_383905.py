def conta_numero(numero,matriz):
    """Função que dado um número e uma matriz conta e retorna quantas 
    vezes o número dado aparece na matriz; int,list->int"""
    soma=0
    for i in matriz:
        if i in matriz:
            soma=soma+list.count(i,numero)
    return soma