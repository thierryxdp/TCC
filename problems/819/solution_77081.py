def filtraMultiplos(list,n):
    multiplos=()
    proximo=0
    while proximo<len(list):
        if list[proximo]%n==0:
            multiplos=multiplos+(list[proximo],)
        proximo=proximo+1
    return multiplos