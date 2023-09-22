def retira_pontuacao(frase):
    
    frase_nova = frase
    frase_nova = str.replace(frase_nova,'...',' ')
    frase_nova = str.replace(frase_nova,'.',' ')
    frase_nova = str.replace(frase_nova,';',' ')
    frase_nova = str.replace(frase_nova,'!',' ')
    frase_nova = str.replace(frase_nova,'?',' ')
    frase_nova = str.replace(frase_nova,':',' ')
    frase_nova = str.replace(frase_nova,',',' ')
    frase_nova = str.replace(frase_nova,'-',' ')
    frase_nova = str.replace(frase_nova,';',' ')
    return frase_nova