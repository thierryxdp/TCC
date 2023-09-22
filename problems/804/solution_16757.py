def filtra_pares(tupla):
    """Funcao que receba uma tupla com quatro elementos inteiros como parâmetro,
    e retorne uma nova tupla contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam."""
    A=int(tupla[0])
    B=int(tupla[1])
    C=int(tupla[2])
    D=int(tupla[3])
    x=()
    if A%2==0:
        x=x+(A,)
    if B%2==0:
        x=x+(B,)
    if C%2==0:
        x=x+(C,)
        
    if d%2==0:
        t=t+(d,)
    return t