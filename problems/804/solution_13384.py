#Start your python function here
def filtra_pares(todos_numeros):
    a,b,c,d = todos_numeros
    nova_tupla = ()
    if int(todos_numeros[0])%2==0:
        nova_tupla = nova_tupla+(todos_numeros[0],)
        return nova_tupla#Start your python function here