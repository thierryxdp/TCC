#da a posição da letra ou string
#str,str,int-->int
def posLetra(st, l, n):
    x=st.find(l)
    while x >= 0 and n> 1:
        x=st.find(1, x + 1)
        n-=1
    return x