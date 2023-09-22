def conta_numero(numero, matriz):
    """funcao que dado um numero inteiro e uma matriz retorna quantas vezes
    o numero dado aparece na matriz."""
    #Armazena a quantidade de vezes o numero aparece
    qtdVezes = 0
    for num in matriz:
        for nume in num:
            if nume == numero:
                qtdVezes +=1
            else:
                pass
    return qtdVezes