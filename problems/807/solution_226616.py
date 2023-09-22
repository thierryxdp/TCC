def conta_frase(frase):
       frase= str.split(frase,'...')
       frase= str.join(".",frase)
      
       frase= str.split(frase,'?')
       frase= str.join(".",frase)
       
       frase= str.split(frase,'.')
       frase= str.join(".",frase)
       
       frase= str.split(frase,'!')
       frase= str.join(".",frase)
       
       frase= str.split(frase,'.')
       frase.remove('')
       num= len(frase)
       return num