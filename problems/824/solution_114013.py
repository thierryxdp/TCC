def uppCons (frase):
    con='b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','z','ç'
    i=0
    while frase[i] < frase:
          if frase[i] in con:
            f=frase.replace(frase[i],frase[i].upper)    
          i=i+1
    return f