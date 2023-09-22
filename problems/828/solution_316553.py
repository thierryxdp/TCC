def primo(n):
    '''Função que dado um número inteiro positivo, verifica se este número é primo ou não retornando um valor booleano;
       int --> boolean'''
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(a,i)
    if (len(a)>2 or n==1):
        return False
    elif(n==2):
        return True
    else:
        return True