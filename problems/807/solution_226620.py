def conta_frase(frase):
      
#1
 frase= str.split(frase,'...')
frase= str.join(".",frase)
# 2
frase= str.split(frase,'?')
frase= str.join(".",frase)
#3
frase= str.split(frase,'.')
frase= str.join(".",frase)
# 4
frase= str.split(frase,'!')
frase= str.join(".",frase)
# mudanca
frase= str.split(frase,'.')
frase.remove('')
um= len(frase)
      
  return num