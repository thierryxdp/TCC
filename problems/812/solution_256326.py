def retira_pontuacao(frase):
   
    s1=str.split(frase,-',',',':',';','.')
    s=str.join(' ',(s1))
    return s