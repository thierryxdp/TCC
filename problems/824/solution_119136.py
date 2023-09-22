def uppCons(frase):
    i=0
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    l=list(frase)
    while i<len(l):
        if l[i] in consoantes:
            l[i]=str.upper(l[i])
            i=i+1
        else:
            i=i+1
    return str.join('',l)