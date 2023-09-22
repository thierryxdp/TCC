def filtra_pares(a):
    S=int(a[0])##as variaveis transformam os elementos da tupla em numeros inteiros
    G=int(a[1])
    H=int(a[2])
    I=int(a[3])
    if S%2==0 and G%2==0 and H%2==0 and I%2==0:
        return (S,G,H,I)
    elif S%2!=0 and G%2==0 and H%2==0 and I%2==0:
        return (G,H,I)
    elif S%2!=0 and G%2==0 and H%2==0 and I%2!=0:
        return (G,H)
    elif S%2!=0 and G%2!=0 and H%2==0 and I%2==0:
        return (H,I)
    elif S%2!=0 and G%2==0 and H%2!=0 and I%2==0:
        return (G,I)
    elif S%2==0 and G%2==0 and H%2==0 and I%2!=0:
        return (S,G,H)
    elif S%2==0 and G%2==0 and H%2!=0 and I%2!=0:
        return (S,G)
    elif S%2==0 and G%2!=0 and H%2==0 and I%2!=0:
        return (S,H)
    elif S%2!=0 and G%2==0 and H%2==0 and I%2!=0:
        return (G,H)
    elif S%2==0 and G%2!=0 and H%2!=0 and I%2!=0:
        return (S)
    elif S%2!=0 and G%2==0 and H%2!=0 and I%2!=0:
        return (G)
    elif S%2!=0 and G%2!=0 and H%2==0 and I%2!=0:
        return (H)
    elif S%2!=0 and G%2!=0 and H%2!=0 and I%2==0:
        return (I,)
    elif S%2!=0 and G%2!=0 and H%2!=0 and I%2!=0:
        return ()
    if S%2==0 and G%2!=0 and H%2==0 and I%2==0:
        return (S,H,I)