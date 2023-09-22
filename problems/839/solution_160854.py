def carros(p, cap=5):
    """caalcula quantos veiculos serao necessarios para uma viagem;
    int, int -> int"""
    n=p/cap
    return max(n)