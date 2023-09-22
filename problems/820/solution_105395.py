#Dado uma str uma letra e um númeor inteiro indica a ocorrência dessa letra
#str,str,int-->int
def posLetra(s, l, n):
    o = 0
    for i in s:
        if s[i] == l:
            o += 1
        if o == n:
            return i
    return -1