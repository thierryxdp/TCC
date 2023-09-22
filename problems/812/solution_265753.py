def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    frase = list(frase.strip(" "))
    list.remove(frase, '-')
    list.remove(frase, ",")
    
    frase=str(frase)
    
    return frase