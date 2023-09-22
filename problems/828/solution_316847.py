def primo(n):
    '''Função que recebe um dado um número inteiro positivo, verifique se este número é primo ou não e retorne um valor booleano
    int->bool'''
    indece=2  
    while indece<n:
        if n%indece!=0:
            indece=indece+1
        
        else:
            return False
    return True