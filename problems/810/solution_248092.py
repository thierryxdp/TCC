def inverte(frase):  
   
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
        frase=lista
        lista = str.split(frase)
        lista.reverse()
        lista.remove('')
        frase = str.join(", ", lista)
        return frase.replace('.',' ')