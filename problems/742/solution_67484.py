def substitui(s,x,i):
    if i>0 and i<=len(s):
        return str(s),int(i),str(x)
    else:
        print('Tente um valor para i, entre 0 e o comprimento da sua string')