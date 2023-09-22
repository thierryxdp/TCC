# substitui a letra da string s definida pelo numero i pelo carctere x 
# funcao substitui
# string, strin, int -> string
def substitui(s,x,i):
    a= len(s)
    if i>=1:
        ss= s[0:1]
        sss= s[i+1:a]
        return str (ss) + str (x) + str (sss)
    else:
        sss= s[i-1:a]
        return str (x) + str (sss)