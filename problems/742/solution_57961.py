def substitui(s,x,i):
    """funçao que na string s substitui o caractere de numero i por x;
    entrada: str, str, int;
    saida: str."""
    
    troca = s [0: i]
    fim = s [i + 1:]
    
    return troca  + str (x) + fim