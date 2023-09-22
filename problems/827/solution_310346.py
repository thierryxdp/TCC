#Função que verifica o número de divisores de um dado numero
def divisores(numero):  
    lista = []
    A = range(numero+1)
    for num in A[1:] :
        if numero % num == 0:
           lista = lista + [numero]
        
    return len(lista)