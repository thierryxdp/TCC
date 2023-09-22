def soma_h(N):
    """Função que retorna a soma de N termos, sendo H=1/1+1/2+1/3+...+1/N. int->int"""
    H=0
    for x in range(1,N+1):
        if x<N+1:
            H+=(1/x)
    return round(H,2)