def uppCons(s):
    'Função que dada uma frase, retorna-a igual, porém com todas as suas consoantes em maiúsculo.'
    'str->str'

    x=s[0:1]
    z=s[1:-1]
    
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
    o=str.replace(e, 'Ì', 'ì')
    p=str.replace(e, 'Î', 'î')
    q=str.replace(e, 'É', 'é')
    r=str.replace(e, 'È', 'è')
    s=str.replace(e, 'Ê', 'ê')
    t=str.replace(e, 'Á', 'á')
    u=str.replace(e, 'À', 'à')
    v=str.replace(e, 'Â', 'â')
    w=str.replace(e, 'Ã', 'ã')
    return w+f