def primo(num):
    '''
Função que dado um numero inteiro positivo, verifica se 
este numero  ́e primo ou não e retorne com um valor booleano.
    int-->boll
    '''
    numero=0
    for i in range(1,num+1):
        if num % i== 0:
            numero=numero+1 
    if numero>2 or numero==1:
        return False
    else:
        return True