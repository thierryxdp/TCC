def retira_pontuacao(frase):
    """ função que, dada uma frase, retira toda a pontuação dela, substituindo por espaço"""
   x= "-" or "," or ":" or ";" or "." or"!" or "?"
    return str.replace(frase,x, " ")