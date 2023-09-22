def faltante(L):
    """Funcao que dada uma lista com N - 1 inteiros de 1 a N, verifica
    qual numero está faltando na sequencia.
    Entrada: list;
    Saida: int;
    
    Parameter:
    L: Lista L de inteiros
    """
    seguinte = 1
    
    while seguinte in L:
    	seguinte = seguinte + 1
    return seguinte