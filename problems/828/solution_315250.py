def primo(numero):
    """Retorna se o numero é primo ou nao;
    	int -> bool"""
    lista = []
    i = 1
    while i <= numero:
        if numero%i==0:
            lista = lista + [i]
        i = i + 1
    if lista == [1,numero]:
        return True
    else:
        return False