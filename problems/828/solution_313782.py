def primo(n):
    """Função que ao receber um número inteiro, retorna se esse número
    é ou não um número primo;
    int -> bool"""
    lista =[]
    for i in range(2,n):
        if n%i == 0:
            list.append(lista,i)
    if len(lista) > 0:
        return False
    else:
        return True