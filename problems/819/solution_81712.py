def filtraMultiplos(a:list,b:int) -> list:
    if a%b == 0:
        return a.pop()