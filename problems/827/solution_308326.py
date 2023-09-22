def qtd_divisores(numero):
    divisao = []
    for i in range(numero):
        
        if numero%(i+1)==0:
            divisao+= [i]
    return len(divisao)