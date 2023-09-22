def qtd_divisores(numero):
    
    valor=1
    valores=[]
    
    while valor<numero:
        if numero%valor==0:
            list.append(valores,valor)
        valor=valor+1
            
    return len(valores)