def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
        
        lista = str.split(frase)
        lista.reverse()
        list.remove(lista,'',')
        frase = str.join(", ", lista)
        return frase.replace('.',' ')