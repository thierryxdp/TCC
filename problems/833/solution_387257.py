def conta_numero(numero,matriz):
    qtd_linhas=len(matriz)
   
    qtd_numeros=0
    for i in range(qtd_linhas):
        if i  not in  qtd_numero:
                qtd_numeros[i]=i.count(numero)
    return qtd_numeros