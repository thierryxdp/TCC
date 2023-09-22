def inverte(frase):  
    def retira_pontuacao(frase):
        frase=frase.replace(',','.')
        frase=frase.replace('?', '.')
        frase=frase.replace('!','.')
        frase=frase.replace('-','.')
    
   
    

    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase.replace('.',' ')