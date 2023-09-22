def faltante(L):
    """Retorna qual numero inteiro do intervalo da lista L está faltando;
       Entrada: list;
       Saida: int;
    """
    intervalo = 1 
    while intervalo in L:
        intervalo = intervalo + 1
    return intervalo