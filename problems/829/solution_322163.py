def soma_h(num):
    """A função calcula e retorna o valor H com N termos;
    int -> float"""
    H = list(range(1, num+1))
    listaH = [1/n for n in H]
    return round(sum(listaH), 2)