def qtd_divisores(num):
    '''Função que retorna a quantidade total de divisores de um número inteiro
    n. Entrada: int. Saída: int'''
    qtd_d=0
    for d in range(1,num+1): #lista de valores de 1 até num, desses quais d sera os divisores 
        if num%d==0:
            qtd_d=qtd_d+1
    return qtd_d