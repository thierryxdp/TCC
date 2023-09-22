def retira_pontuacao(frase):
    frase1=frase.join(':',frase)
    frase2=frase1.join(';',frase)
    frase3=frase2.join('.',frase)
    frase4=frase3.join(',',frase)
    frase5=frase4.join('-',frase)
    return frase5