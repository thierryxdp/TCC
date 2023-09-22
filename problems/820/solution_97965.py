def posLetra(frase,letra,n):
    y=0
    x=0
    if str.count(frase,letra)<n:
        return -1
    else:
        while y<n:
          if letra==frase[x]:
              y=y+1
          x=x+1
        return x-1