'''você me dá um número retorno True se for primo e se não for retorno False
int -> bool'''
    contador_de_divisores=0
    for x in range(1,num + 1):
        if numero % x == 0:
            contador_de_divisores +=1
    if contador_de_divisores == 2:
        return True
    else:
        return False +=1