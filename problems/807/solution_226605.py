def conta_frase(frase):
       ''' funcao que recebe uma strng e retornaa quantidade  varias frases
       ; str=> int '''
        #1
       frase= str.split(frase,'...')
       frase= str.join(".",frase)
       #2
       frase= str.split(frase,'?')
       frase= str.join(".",frase)
       #3
       frase= str.split(frase,'.')
       frase= str.join(".",frase)
       #4
       frase= str.split(frase,'!')
       frase= str.join(".",frase)
       #mud
       frase= str.split(frase,'.')
       frase.remove('')
       num= len(frase)
      
       return num