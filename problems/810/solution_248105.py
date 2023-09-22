def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
         
            
         
        lista = str.split(frase)
        
        frase = str.join(" ", lista)
        return frase.replace('.',' ')