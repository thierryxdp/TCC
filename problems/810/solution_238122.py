def retira_pontuacao(frase):
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'-',' ')
    
    frase=str.lower(frase)
    lista=str.split(frase)
    lista=lista[::-1]
    espaco=' '
    frase=espaco.join(lista)
    return frase