# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# int, int, int, int -> int
def filtra_pares(a,b,c,d):
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        t=[a,b,c,d]
        return t
    if a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        t=[a,b,c]
        return t
    if a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        t=[a,b,d]
        return t
    if a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        t=[a,c,d]
        return t
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        t=[b,c,d]
        return t