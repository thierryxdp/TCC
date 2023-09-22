def conta_frases(texto):
   x=str.replace(str.replace(str.replace(str.replace(texto,'...','#'),'.','#'),'!','#'),'?','#')
   return str.count(x,'#')