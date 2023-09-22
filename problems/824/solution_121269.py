def uppCons(f):
    '''Retorna um texto atualizado com todos as consoantes em maiuscula e as demais conforme informadas.
    str->str'''
    x=0
    n=''
    while x<len(f):
      if f[x]!="a" and f[x]!="e" and f[x]!="i" and f[x]!="o" and f[x]!="u":
        n += str.upper(f[x])
      else :
        n+=f[x]
      x+=1
    return n