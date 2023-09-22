#Start your python function here
"essa funcao recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla com apenas pares de uma tupla origial; str, str -> int"
def filtra_pares(t):
    n=()
    if t[0] % 2 == 0:
        n = n + (t[0],)
    if t[1] % 2 == 0:
        n = n + (t[1],)
    if t[2] % 2 == 0:
        n = n + (t[2],)
    if t[3] % 2 == 0:
        n = n + (t[3],)
    
    return n