def retira_pontuacao(frase):
    """ função que, dada uma frase, retira toda a pontuação dela, substituindo por espaço"""
    return str.replace(frase,("-" or "," or ":" or ";" or "." or"!" or "?"), " ")