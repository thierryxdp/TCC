def primo(num):
    """função que recebe um número qualquer (num) de entrada e verfica
    se ele é primo ou não é. Tal que esse número seja ;
    int->bool"""
    qtd_numeros=0
    numeros = range(2,num+1)
    for n in numeros:
        if num%numeros[n-2]==0:
            qtd_numeros=qtd_numeros+1
    if qtd_numeros<2:
        return True
    else:
        return False