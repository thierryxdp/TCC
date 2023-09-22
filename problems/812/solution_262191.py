def retira_pontuacao(frase):
    
    frase_nova = frase
    frase_nova = str.replace(frase,'...',' ')
    frase_nova = str.replace(frase,'.',' ')
    frase_nova = str.replace(frase,';',' ')
    frase_nova = str.replace(frase,'!',' ')
    frase_nova = str.replace(frase,'?',' ')
    frase_nova = str.replace(frase,':',' ')
    frase_nova = str.replace(frase,',',' ')
    frase_nova = str.replace(frase,'-',' ')
    frase_nova = str.replace(frase,';',' ')
    return frase_nova