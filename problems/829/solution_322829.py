def soma_h (N):
    """dado N como parametro, calcula o valor de H com N termos;
    int-> float"""
    n=list(range(1,N+1))
    p=0
    aux=0
    for n[p]in list(range(1,N+1)):
        aux=aux+1/n[p]
        p+=1
        
    return aux