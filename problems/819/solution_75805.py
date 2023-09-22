def filtraMultiplos(lista, n):
    """Retorna uma lista apenas com os multiplos de n que estao na lista dada;
       Entrada:
       Saida:
    """
    if len(lista)%n==0:
        return [len(lista)]