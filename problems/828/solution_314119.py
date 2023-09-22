def primo(n):
    """funcao que recebe um numero inteiro positivo, 
    determina quais sao seus divisores,se tem mais de 2 divisores não é primo. 
    Retorna em booleano se ele é primo ou nao. 
    entrada->int
    saida-> bool"""
    primo=[]
    for i in range(1,n+1):
        if n%i==0:
            primo=primo +[i]
    if len(primo)> 2:
        return False
    else: return True