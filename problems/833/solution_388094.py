def conta_numero(inteiro,matriz):
    'Função que recebe um número inteiro e uma matriz e retorna quantas vezes esse número apareceu nela.'
    'int,list->int'

    c=0

    for linha in matriz:
        for numero in linha:
            if numero==inteiro:
                c=c+1
                
    return c