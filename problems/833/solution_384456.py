def conta_numero(numero,matriz):
    '''Conta quantas vezes um numero inteiro aparece
    em uma matriz composta de numeros inteiros;
    int,list(list) -> int'''
    contador = 0
    for i in matriz:
       for j in i:
          if j == numero:
             contador = contador + 1
    return contador