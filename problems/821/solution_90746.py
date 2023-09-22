def fatorial(num):
    
    """
    int--->int
    Se da uma variavel para o numero na entrada.Enquanto o numero sempre
    diminui 1 a cada operação,a variavel serve para manter o valor das 
    multiplicacoes anteriores, fazendo com que seja possivel a formacao do codigo
    
    """
    
    
    i=num
    
    while (num-1)>1:
        num-=1
        i=(num)*i
        
    return i