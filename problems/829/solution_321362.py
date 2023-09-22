def soma_h(n):
    """calcula o valor de h com n termos;
    int, -> float"""
    
    h= 0
    for(int i=1; i<=n; i++) {
     h = h + (double)1/i
        return h