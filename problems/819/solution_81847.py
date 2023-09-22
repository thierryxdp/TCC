def filtraMultiplos(a:tuple[int],b:int) -> list:
    i=0
    while i < len(a):
        i+=1
        multiplos = []
        if a[i]%b == 0:
            multiplos.append(a[i])
    return multiplos