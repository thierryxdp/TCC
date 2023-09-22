def primo(n):
    '''primo recebe um numero inteiro e devolve um valor booleano
    determine se o numero n é primo e se for retorna true 
    int --> bool'''
    
    lista = []

    for numero in range(1,n+1):
        if n%numero == 0 and n%n==0:
            list.append(lista,numero)
        
    return len(lista)==2