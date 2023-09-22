def soma_h(n):
# Funcao que recebe como entrada um numero inteiro e retorna um float com 2 casas decimais como reasultado de uma soma H 
    
    soma = 0
    for i in range(1,n+1):
        soma = soma+1/i
    soma_2 = round(soma,2)
    return soma_2