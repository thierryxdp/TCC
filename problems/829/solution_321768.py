def soma_h(n):
    """Função que calcula e retorna o Valor H com N
    termos nde N é o número inteiro dado como paramêtro de 
    entrada.
    int --> Float;
    """
    H=[]
    for i in range(1,n+1):
        list.append(H,1/i)
        
    H=sum(H)
    H=round(H,2)
    return H