def fatorial(num):
    '''Função que dado um número inteiro como entrada,
    calcula o fatorial deste número; int -> int'''
    
    copia = num
    b = 1
    contagem = 0
    while contagem+1 < copia:
            num = num * b
            b = b+1
            contagem = contagem + 1
    return num