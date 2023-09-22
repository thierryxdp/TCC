def conta_numero(numero,matriz):
    '''Função que dado um numero e uma matriz retorna quantas vezes esse numero aparece
    entrada:list
    saida:int'''
    contador=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
            	contador=contador+1
    return contador