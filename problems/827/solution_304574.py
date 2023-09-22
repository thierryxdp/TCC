def qtd_divisores(n):
    '''Função que recebe um inteiro e retorna quantos divisores esse número
possui
Entrada(int)
Saída(int)'''
    divisores=0
    for i in range(1,n + 1):
        if n%i==0:
            divisores+=1
    return divisores