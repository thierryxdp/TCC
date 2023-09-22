def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
         
            
       
        lista.reverse()
        frase = str.join(" ,", lista)
        return frase.replace('.',' ')