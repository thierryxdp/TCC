def conta_numero(numero,matriz):
    'dado um número inteiro e uma matriz, retorne a quantidade de vezes que este numero aparece na matriz. int,list(list)-->int'
    qtd=0
    for listas in matriz:
        for elemento in listas:
            if elemento==numero:
                qtd=qtd+1
    return qtd