def primo(numero):
    '''Função que retorna  e  valor booleano se o  número é primo ou não
    entrada= int
    saida= bool'''
    if numero % 2==0 or numero % 3== 0 or numero % 7== 0 or numero % 11==0 or numero % 13==0 or numero % 17==0 or numero % 71 ==0:
        
        return False
    else:
        return True