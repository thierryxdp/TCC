def soma_h(n):
    '''funcao que, dado um numero inteiro positivo, retorna o valor da soma com no 
    maximo 2 casas decimais dos inversos dos numeros inteiros positivos que sao menores 
    ou iguais a n;
    int->float'''
    soma=0
    for numero in range(1,n):
        if numero < n:
            soma = soma + 1/numero        
    return round(soma,2)