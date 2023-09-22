def conta_frases(x):
    a=str.replace(x,'...','#')
    b=(len(str.split(a,'#'))-1)
    c=(len(str.split(a,'.'))-1)
    d=(len(str.split(a,'!'))-1)
    e=(len(str.split(a,'?'))-1)
   
    return b+c+d+e