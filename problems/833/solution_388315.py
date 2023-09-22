def conta_numero(num,matriz):
    '''dado um numero inteiro e uma matriz de numeros inteiros, conta e retorna quantas vezes aquele numero aparece na matriz'''
    qtd_vezes=0
    for i in matriz:
       
            
                qtd_vezes=qtd_vezes+i.count(num)
    return qtd_vezes