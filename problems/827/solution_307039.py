def qtd_divisores(N):
    '''funcao que dado um numero N, sendo este um inteiro, identifica quantos divisores esse numero tem e retorna a quantidade desses divisores;
       int-> int'''
    quantidade= 0
    for divisor in range(N+1):
        if N%divisor== 0:
            quantidade= quantidade+1
    return quantidade