def substitui(s,x,i):
    palavra = s
    return palavra [0: i] + str (x) + palavra [(i+1): len(palavra)]