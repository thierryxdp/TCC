def filtra_pares(tupla1):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    if a%2==0:
        tupla1 = [a,]
    if b%2==0:
        tupla1 = tupla1 + [b,] 
    if c%2==0:
        tupla1 = tupla1 + [c,] 
    if d%2==0:
        tupla1 = tupla1 + [d,] 
    return tupla1