def filtraMultiplos(l,n):
    i = 0
    multiplos = 0
    nova_lista= ()
    while multiplos<=len(l):
           if l[i]%n == 0:
            multiplos = multiplos + 1
            nova_lista = nova_lista + multiplos
            i = i + 1
            else:
            0
    return nova_lista