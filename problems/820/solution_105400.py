#Dado uma
#str,str,int-->int
def posLetra(st, l, n):
    x = st.find(l)
    while x >= 0 and n > 1:
        pos = st.find(l, x + 1)
        n -= 1
    return pos