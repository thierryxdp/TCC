def filtraMultiplos(a:tuple[int],b:int) -> list[int]:
    multiplos = []
    i=0
    while i < len(a):
        if a[i]%b == 0:
            multiplos.append(a[i])
        i+=1
    return multiplos