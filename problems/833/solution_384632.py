def conta_numero(numero,matriz):
    '''Função que retorna quantas vezes o numero 
    		aparece na matriz
            num, lista -> num '''
    contador = 0
    for num in matriz:
        for vezes in num:
            if vezes == numero:
                contador += 1
    return contador