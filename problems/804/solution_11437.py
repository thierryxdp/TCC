def filtra_pares(a):
    tupla=()
    if a[0]%2==0:
        tupla=tupla+(a[0],)
        if a[1]%2==0:
            tupla=tupla+(a[1],)
            if a[2]%2==0:
                tupla=tupla+(a[2])
                if a[3]%2==0:
                    tupla=tupla+(a[3],)
                    return tupla