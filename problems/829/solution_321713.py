def soma_h(n) : 
    """Calcula e retorna o valor H com N termos onde N
    é inteiro e dado como entrada, 
    exemplo H = 1/1 + 1/2 + 1/3 + ... + 1/N ; 
    int -> float"""
    a = list(range(1,n+1))
    resultado = []
    for x in a : 
        list.append(resultado,1/x)
        
    return round(sum(resultado),2)