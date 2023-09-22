def faltante(L):
    ''' Dado uma lista L de numeros inteiros não repetidos
    referindo-se as peças do quebra cabeça completo,
    retorna qual numero da peça que está faltando;
    list-> int'''
    x= len (L) + 1
    somatotal= x * (x + 1) // 2
    return somatotal - sum(L)