def soma_h(N):
    """funcao que calcula e retorna o valor de H com N termos;
    Entrada: int
    Saida: float"""
    H=0
    
    for i in range(N):
        H+=1/(1+i)
    
    return round(H,2)