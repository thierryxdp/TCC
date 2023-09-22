r = []
c = 0
def uppCons(frase):
    while c<=len(frase):
        if frase[c]=='M':
            r.append(frase[c])
    c+=1
   	return r