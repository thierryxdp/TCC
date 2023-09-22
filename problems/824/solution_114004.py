def uppCons (frase):
    con='b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','z','ç'
    i=0
    while frase[i] < frase:
          if frase[i] in con:
          i=i+1
    return frase.replace(frase[i],frase[i].upper)