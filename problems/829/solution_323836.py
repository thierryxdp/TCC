def soma_h(n):
    '''Calcula e retorna o valor de H com n termos onde N é inteiro e dado como entrada
    int->int'''
    
    H=0
    
    for i in range(1,n+1):
        H=H+(1/(i))
    return round(H,2)