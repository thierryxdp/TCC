def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento 
    da string. Após, retorna uma string igual a s, exceto pelo elemento da posição i,
    que deve ser substituído pelo caractere x.
    Assinatura: str, int, int -> str
    Casos de teste:
    substitui("cavalo", "x", 2) == 'caxalo'
    substitui("apaixonado", "1", 4) == 'apai1onado'
    """
    return s[:i] + x + s [i+1:]