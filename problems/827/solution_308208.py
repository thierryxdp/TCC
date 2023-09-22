def qtd_divisores(num):
    divisores = []
    for menor in list(range(0,num+1)):
        if 10%menor == 0:
        	divisores.append(menor)
    return len(divisores)