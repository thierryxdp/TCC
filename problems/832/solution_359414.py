def eh_quadrada(x):
    """Retorna se a matriz é quadrada;
       Entrada: list;
       Saída: bool;
    """
    if x==[]:
            return True
    for i in range(len(x)):
        if len(x)==len(x[i]):
            return True
        else:
            return False