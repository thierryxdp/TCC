def colchao1(medidas,H,L):
    m=sorted(medidas)
    m1=max(m)
    m2=m.remove(max(m))
    m3=max(m)
    p=[H,L]
    p1=max(p)
    p2=min(p)
    
    if m1<p1 and m3<p2:
        return True 
    elif m1<p1 and m3>p2:
        return False
    elif m1<p1 and m3==p2:
        return False
    elif m1>p1 and m3<p2:
        return False
    elif m1==p1 and m3<p2:
        return False
    elif m1>p1 and m3>p2:
        return False
    elif m1==p1 and m3==p2:
        return False

# Escolha nomes elucidativos para suas variáveis