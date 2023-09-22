def primo(numero):
    '''Retorna se o numero dado é primo ou nao;
       Entrada: int;
       Saida: bool;
    '''
    for x in range(1, numero-1):
        if x == 2:
            return False
        if numero%x == 0:
            lista = []
            list.append(lista, x)
            if len(lista) == 1:
                return True