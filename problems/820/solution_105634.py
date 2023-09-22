def posLetra(st, 1, n):
    x = st.find(1)
    while x >= 0 and n >1:
        x = st.find(1, x + 1)
        n -= 1
    return x