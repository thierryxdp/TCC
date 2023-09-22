def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
        
        lista = str.split(frase)
        lista.reverse()
       
        frase = str.partition(lista, '.')
        
        return  frase.replace('.',' ')