def conta_frases(a):
    b=(len(str.split(a,'.'))-1)
    c=((len(str.split(a,'...')))//3)
    d=(len(str.split(a,'!'))-1)
    e=(len(str.split(a,'?'))-1)
   
    return b+c+d+e