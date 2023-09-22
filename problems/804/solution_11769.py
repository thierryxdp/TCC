def filtra_pares(tupla):
    """Função que dado uma tupla com quatro parâmetros, retornará apenas os pares na mesma ordem original."""
    tupla=[(a,b,c,d)]
    if a%2==0:
        tupla = [a,]
    if b%2==0:
        tupla = tupla + [b,] 
    if c%2==0:
        tupla = tupla + [c,] 
    if d%2==0:
        tupla = tupla + [d,] 
    return tupla1