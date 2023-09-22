def qtd_divisores(num):
    """função que recebe um número de entrada (num)
    e calcula quantos divisores possíveis esse número
    tem, tal que retorne a quantidade em números
    em números inteiros;
    int->int"""
    qtd_numeros=0
    for n in range(1,num+1):
        if num%numeros[n-1]==0:
            qtd_numeros=qtd_numeros+1
    return qtd_numeros