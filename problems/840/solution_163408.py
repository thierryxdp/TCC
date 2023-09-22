def bolos(a, b, c):
    """Cclcula quantos bolos Jõao cosnegue fazer de forma exata de acordo com a quantidade de ingrediaentes
    farinha: a, ovos: b, leite: c """
    f = a//2
    o = b//3
    l = c//5
    list = [f, o, l]
    if f==0 or o==0 or l==0:
        return 0
    elif f!=o or f!=l or l!=o:
        return(min(list))
    elif f==o==l:
        return f