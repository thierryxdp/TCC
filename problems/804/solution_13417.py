def filtra_pares(todos_numeros):
    a,b,c,d = todos_numeros
    nova_tupla = ()
    if int(todos_numeros[0])%2==0:
        nova_tupla = nova_tupla+(todos_numeros[0],)
    if int(todos_numeros[1])%2==0:
        nova_tupla = nova_tupla+(todos_numeros[1],)
    if int(todos_numeros[2])%2==0:
        nova_tupla = nova_tupla+(todos_numeros[2],)
    if int(todos_numeros[3])%2==0:
        nova_tupla = nova_tupla+(todos_numeros[3],)
        return nova_tupla[0:-1]