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
    espaco=' '
    return espaco.join(lista)