def soma_h(n):
    """"função que calcula e retorna o valor H com N termos onde N é um parâmetro inteiro.
    
    int -> float
    
    exemplos:
    soma_h(2)==1.5
    soma_h(3)==1.83"""
    soma=0
    for i in range(1,n+1):
        soma=soma+1/i
    return round(soma,2)