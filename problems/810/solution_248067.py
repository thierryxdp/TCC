def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
        
        lista = str.partition(frase, '.')
        lista.reverse()
        frase = str.join('.', lista)
        frase=frase.lower()
        return  frase.replace('.',' ')