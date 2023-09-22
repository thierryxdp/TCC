def filtaMultiplos(n):
    lista=()
    numero=0
    while numero<len(n):
        if n[numero]%2==0:
            lista=lista+(n[numero],)
        numero=numero+1
    return lista