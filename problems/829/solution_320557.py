def soma_h(N):
    """funcao que calcula e retorna o valor de H com N termos;
    Entrada: int
    Saida: float"""
    H=0
    
    for i in range(N):
        H+=1/(1+N)
    H=round(H,2)
    return H