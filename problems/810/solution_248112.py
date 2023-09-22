def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
         
            
         
        lista = str.split(frase)
        frase=lista.reverse(frase)
        
        return frase