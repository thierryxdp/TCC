def uppCons(frase):
    "..."
    i=0
    consoante=''
    while i < len(frase):
          if frase[i] not in 'AEIOUaeiouaéíóú':
                consoante=consoante+str.upper(frase[i])
          else:
           consoante=consoante+frase[i]
          i=i+1
    return consoante