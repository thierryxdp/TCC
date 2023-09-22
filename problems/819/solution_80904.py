def filtraMultiplos(l,n):
    i = 0
    multiplos = 0
    nova_lista= ()
    while (len(l)%n)==0:
           if l[i]%n == 0:
            multiplos = multiplos + 1
            nova_lista = nova_lista + multiplos
            i = i + 1
            else:
            i = i + 1
    return nova_lista