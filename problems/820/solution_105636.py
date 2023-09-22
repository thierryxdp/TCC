def posLetra(st, l, n):
    x = st.find(l)
    while x >= 0 and n >1:
        x = st.find(l, x + 1)
        n -= 1
    return x