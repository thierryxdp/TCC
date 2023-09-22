def qtd_divisores(n):
#Funcao que dado um inteiro, retorna um inteiro que corresponde ao numero de divisores do numero inserido    
    cont= 0
    for i in range(1, n+1):
        if n % i == 0:
            cont+=1
    return cont