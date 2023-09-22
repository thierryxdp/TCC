def retira_pontuacao(frase):
    k=str.split(txt,'-')
    frase1=str.join(' ',k)
    frase2=str.split(frase1,';')
    frase3=str.join(' ',frase2)
    frase4=str.split(frase3,',')
    frase5=str.join(' ',frase4)
    frase6=str.split(frase5,'.')
    frase7=str.join(' ',frase6)
    frase8=str.split(frase7,':')
    frase=str.join(' ',frase8)
    return frase