def filtraMultiplos(m):
    valores_lista=(m[0],m[1],m[2],m[3])
    multiplos= tuple(filter(lambda m: m%m==0, valores_lista))
    return multiplos