def uppCons(f):
    '''Retorna um texto atualizado com todos as consoantes em maiuscula e as demais conforme informadas.
    str->str'''
    x=0
    n=''
    while x<len(f):
      if f[x]!="a" and f[x]!="e" and f[x]!="i" and f[x]!="o" and f[x]!="u" and f[x]!="á" and f[x]!="é" and f[x]!="í" and f[x]!="ó" and f[x]!="ú" and f[x]!="â" and f[x]!="ê" and f[x]!="õ" and f[x]!="ô" and f[x]!="ã":
        n += str.upper(f[x])
      else :
        n+=f[x]
      x+=1
    return n