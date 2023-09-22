def conta_numero(numero,matriz):
    '''função que dado um numero inteiro e uma matriz de tamanho qualquer, retorna quantas vezes o numero aparece
    (numero,matriz)=int,matriz
    saida = '''
    s=0
    for l in matriz:
        s+=l.count(numero)
    return s