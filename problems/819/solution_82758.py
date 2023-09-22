def filtraMultiplos(lista, n):
    rep= 0
    list_final= []
    while rep < len(lista):
        final= lista[rep]%n
        if final ==0:
            list_final= lista[rep]+ list_final
    return list_final