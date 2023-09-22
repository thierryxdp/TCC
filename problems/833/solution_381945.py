def conta_numero(numero,matriz):
    '''Função que dado um numero inteiro e uma matriz,retorna quantas vezes esse 
    numero aparece na matriz. int,list->int'''
    ocorrencias=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                ocorrencias=ocorrencias+1
    return ocorrencias