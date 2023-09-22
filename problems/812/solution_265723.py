def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    return frase.replace("-" , "," ,  ":" , ";")