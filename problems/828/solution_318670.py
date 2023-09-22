def primo(numero):
    ''' funçao que dado um numaro inteiro positivo , verifica 
    se este numero é primo ou não .retorna um valor booleano;
    int -> bool'''
    divisores =[]
    for i im eange(numero+1):
        if numero%(i+1)==0
            divisores += [i+1,]
    return len(divisores)==2