def media_matriz(matriz):
    """Recebe uma matriz matemática e retorna a média de todos os números da matriz
       com exatamente duas casas decimais de precisão.
       list->float

       Parameters:
       matriz: Uma matriz matemática."""
    numerador=0
    denominador=0
    for l in matriz:
        for n in l:
            numerador=numerador+n
            denominador=denominador+1
    return round(numerador/denominador,2)