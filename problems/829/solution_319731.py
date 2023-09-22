def soma_h(n):
    ''' Recebe um número inteiro 'n';
Retorna a soma dada com 2 casas decimais;
1 + 1/2 + 1/3 + ... + 1/n;
int => float'''
    termo = 1/n
    soma = 0
    while termo < 1:
        termo = 1/n
        soma = soma+termo
        n = n-1
    return round(soma,2)