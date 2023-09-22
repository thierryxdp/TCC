def primo(numero):
    """função que retorna se um numero é primo ou não
    int -> bool"""
    lista=[]
    for n in range(2,numero):
        if (numero%n)==0:
            lista.append(n)
    if len(lista) > 0:
        return False
    else:
        return True