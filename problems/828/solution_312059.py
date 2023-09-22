def primo(numero):
    '''Retorna se o numero dado é primo ou nao;
       Entrada: int;
       Saida: bool;
    '''
    lista = []
    for x in range(1, numero+1):
        if numero == 2:
            return True
        if numero%x == 0:
            list.append(lista, x)
    if len(lista)> 2:
        return False
    else:
        return True