def soma_h(n):
    """Funcao que calcula a soma de n termos sobre 1;
    int -> float"""
    
    lista = []
    
    for i in range(1,n+1):
        lista.append(1/i)
    
    return round((sum(lista)),2)