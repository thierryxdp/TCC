# Função que retorna uma tupla com os valores pares 
# ass: tupla(int,int,int,int)-->tupla
# testes: filtra_pares(2,8,9,1)==(2,8); filtra_pares(5,10,8,6)==(10,8,6)
def par(s):
    return bool(s%2==0)

def filtra_pares(s):  
    ret=()
    if par(s[0]):
        ret=ret+s[0]
    if par(s[1]):
        ret=ret+s[1]
    if par(s[2]):
        ret=ret+s[2]
    if par(s[3]):
        ret=ret+s[3]
    return ret