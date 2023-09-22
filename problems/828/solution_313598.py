def primo(num):
    """Função que retorna se um numero é primo ou não
    int->bool"""
    numeros_primos = []
    for x in range(1,num+1):
        if num%x==0:
            list.append(numeros_primos,x)
    if len(numeros_primos) == 1:
        return True
    elif len(numeros_primos) == 2:
        return True
    else:
        return False