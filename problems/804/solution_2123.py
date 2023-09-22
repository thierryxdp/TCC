#Start your python function here
def filtra_pares(a):
    even=()## tupla de numeros pares:
    if a[0]%2==0:##faz o modulo com 2 de todos os numeros e se for 0,coloca ela no numero pares
        even+=(a[0],)
    if a[1]%2==0:
        even+=(a[1],)
    if a[2]%2==0:
        even+=(a[2],)
    if a[3]%2==0:
        even+=(a[3],)
        return even