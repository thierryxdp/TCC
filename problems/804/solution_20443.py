def filtra_pares(f):
    pares_novos=()
    if f[0]%2==0:
        pares_novos=pares_novos+(f[0],)
    if f[1]%2==0:
        pares_novos=pares_novos+(f[1],)
    if f[2]%2==0:
        pares_novos=pares_novos+(f[2],)    
    if f[3]%2==0:
        pares_novos=pares_novos+(f[3],)
        return pares_novos
    else:
        return ()