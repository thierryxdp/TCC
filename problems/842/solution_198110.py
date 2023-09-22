def pontos_por_time(lista):
    """..."""
    a = lista[0]
    b = lista[1]
    c = a[0]
    d = a[1]
    e = a[2]
    f = b[0]
    g = b[1]
    h = b[2]
    j = e[0]
    k = e[1]
    m = h[0]
    n = h[1]
    if k<j and n>m:
        return {d:0, c:6}
    if k>j and m>n:
        return {d:6, c:0}
    if k>j and m<n and 'Fluminantos' not in lista:
        return {c:3, d:3}
    if k<j and n<m and 'Fluminantos' not in lista:
        return {c:3, d:3}
    if k==j and n<m:
        return {d:4, c:1}
    if k==j and n>m:
        return {c:4, d:1}
    if k>j and n==m:
        return {d:1, c:4}
    if k<j and n==m:
        return {c:4, d:1}
    if k==j and n==m:
        return {c:2, d:2}
    if k>j and m<n and 'Fluminantos' in lista:
        return {d:3, c:3}
    if k<j and n<m and 'Fluminantos' in lista:
        return {d:3, c:3}