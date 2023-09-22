def primo(num):
    '''
       Dado um número a função verifica esse número é primo 
       ou não e retorna True quando o número é primo e False
       quando o número não é primo.
       int -> bool
    '''
    primo = True
    for i in range(2,num-1):
        if num%i == 0:
            primo = False
    return primo