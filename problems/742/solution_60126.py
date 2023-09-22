def substitui(s, x, i):
    
    """Essa função serve para inserir uma string, uma determiada letra, e 
    uma posição para se substituir.
    para s: str -> str  Texto inicial
    para x: str -> str Caractere que alterará o texto
    para i: int -> int Posição onde o caractere (x) substituirá em (s)"""
    
    return s[:i] + x + s[i+1:]