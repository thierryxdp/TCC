def primo(num):
    """Função que, dado um número, verifica se o número
    é primo ou não.
    int->bool"""
    lista=[]
    for i in range(1,num+1):
        if num % i == 0:
            lista.append(i)
            if len(lista)<=2:
                if 1 and num in lista:
                    return True
            else:
                return False