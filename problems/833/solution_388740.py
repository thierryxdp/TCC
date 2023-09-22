def conta_numero(numero,matriz):
    'função que recebe um número inteiro e uma matriz e retorna quantas vezes'
    'o número aparece na matriz. int->int'
    m=0
    quantas_vezes=0
    while m<len(matriz):
        quantas_vezes+=(list.count(matriz[m],numero))
        m+=1
    return quantas_vezes