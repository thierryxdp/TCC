def conta_numero(numero,matriz):
    """ Funçao que dado um numero inteiro e uma matriz de inteiros de 
    qualquer tamanho, retorna quantas vezes o numero aparece na matriz"""
    
    qtd_vezes=0
    
    for i in matriz:
        
        for numero in i:
            if numero == matriz:
                qtd += 1
    return qtd_vezes