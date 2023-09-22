def conta_numero(numero,matriz):
    '''dada uma martiz, podemos saber com essa funçao 
    quanos termos de um valor especifico se encontram
    dentro da matriz dada
    int, lista--->int'''
    x=0
    if len(matriz)==0:
        return 0
    else:
        numeroLinhas=len(matriz)
        numeroColunas=len(matriz[0])
        for i in range(len(matriz)):
            if numero in matriz[i]:
                x=x+m[i].count(numero)
        return x