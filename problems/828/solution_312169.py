def primo(numero):
    divisores=1

    for i in range(numero):
        if (i!=0) and (numero%i == 0) :
            divisores+=1
    
    if divisores>2:
        return False
    else:
        return True