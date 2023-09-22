def qnd_divisores(num):
    '''recebe um numero e retorna a qtd de divisores'''
    resultado = [i for i in range(1, numero + 1) if numero % i ==0]
    
    return len(resultado)