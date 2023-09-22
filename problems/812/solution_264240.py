def retira_pontuacao(frase):
      
    frase1=str.join(' ',str.split(frase,','))

    frase2=str.join(' ',str.split(frase1,'.'))
    return str.join(' ',str.split(frase2,'-'))