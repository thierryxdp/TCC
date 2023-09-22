def primo(n):
    ''' função que dado um número inteiro positivo,
    verifique se este número é primo ou não,
    e retorne um valor booleano. int -> boolean''' 
    r= True
    for i in range(2,n):
        if n % i == 0:
            r = False
    return r