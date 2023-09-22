def filtra_pares(a):
    S=int(a[0])
    G=int(a[1])
    H=int(a[2])
    I=int(a[3])
    if S%2==0 and G%2==0 and H%2==0 and I%2==0:
        return (S,G,H,I)
    if S%2!=0 and G%2==0 and H%2==0 and I%2==0:
        return (G,H,I)
    if S%2!=0 and G%2==0 and H%2==0 and I%2!=0:
        return (G,H)
    if S%2!=0 and G%2!=0 and H%2==0 and I%2==0:
        return (H,I)
    if S%2!=0 and G%2==0 and H%2!=0 and I%2==0:
        return (G,I)
    if S%2==0 and G%2==0 and H%2==0 and I%2!=0:
        return (S,G,H)
    if S%2==0 and G%2==0 and H%2!=0 and I%2!=0:
        return (S,G)
    if S%2==0 and G%2!=0 and H%2==0 and I%2!=0:
        return (S,H)
    if S%2!=0 and G%2==0 and H%2==0 and I%2!=0:
        return (G,H)
    if S%2==0 and G%2!=0 and H%2!=0 and I%2!=0:
        return (S,)
    if S%2!=0 and G%2==0 and H%2!=0 and I%2!=0:
        return (G,)
    if S%2!=0 and G%2!=0 and H%2==0 and I%2!=0:
        return (H,)
    if S%2!=0 and G%2!=0 and H%2!=0 and I%2==0:
        return (I,)
    if S%2!=0 and G%2!=0 and H%2!=0 and I%2!=0:
        return ()
    if S%2==0 and G%2!=0 and H%2==0 and I%2==0:
        return (S,H,I)