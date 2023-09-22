def filtraMultiplos(l,n):
    i = 0
    multiplos = 0
    nova_lista= ()
    while (len(l)%n)==0:
        if l[i]==0:
            multiplos = multiplos + i
            nova_lista = multiplos  
        else:
            i = i + 1 
        return nova_lista