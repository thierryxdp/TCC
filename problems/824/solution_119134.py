def uppCons(frase):
    i=0
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    l=list(frase)
    while i<len(l):
        if l[i] in consoantes:
            i=i+1
            l[i]=str.upper(l[i])
        else:
            i=i+1
    return str.join('',l)