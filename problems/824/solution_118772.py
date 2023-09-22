def uppCons(con):
    'Função que dada uma frase, retorna-a igual, porém com todas as suas consoantes em maiúsculo.'
    'str->str'

    x=con[0:1]
    z=con[1:]

    if x in 'bcdfghjklmnpqrstvwxyz':
        x=str.upper(x)
    
    a=str.upper(z)
    b=str.replace(a, 'A', 'a')
    c=str.replace(b, 'E', 'e')
    d=str.replace(c, 'I', 'i')
    e=str.replace(d, 'O', 'o')
    f=str.replace(e, 'U', 'u')
    g=str.replace(f, 'Ú', 'ú')
    h=str.replace(g, 'Ù', 'ù')
    i=str.replace(h, 'Û', 'û')
    j=str.replace(i, 'Õ', 'õ')
    k=str.replace(j, 'Ó', 'ó')
    l=str.replace(k, 'Ò', 'ò')
    m=str.replace(k, 'Ô', 'ô')
    n=str.replace(m, 'Í', 'í')
    o=str.replace(n, 'Ì', 'ì')
    p=str.replace(o, 'Î', 'î')
    q=str.replace(p, 'É', 'é')
    r=str.replace(q, 'È', 'è')
    s=str.replace(r, 'Ê', 'ê')
    t=str.replace(s, 'Á', 'á')
    u=str.replace(t, 'À', 'à')
    v=str.replace(u, 'Â', 'â')
    w=str.replace(v, 'Ã', 'ã')
    return x+w