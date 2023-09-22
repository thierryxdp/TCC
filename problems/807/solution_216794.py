def conta_frases(frase):
    s=frase
    f=s.replace('. ',' ',)
    f=f.replace('? ',' ',)
    f=f.replace('... ',' ',)
    k=f.replace('! ',' ',)
   
    return len(k)