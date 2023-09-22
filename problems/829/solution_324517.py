def soma_h(n):
    '''recebe o número n de termos em uma soma = 1 + 1/2 + 1/3 + ... + 1/n e retorna o valor da soma com aproximação de duas casas decimais;
    int -> float'''
    soma = 1
    d = 2
    a = 1/d
    
    while d <= n:
        soma = soma + a
        d = d + 1
        a = 1/d
        
    return round(soma,2)