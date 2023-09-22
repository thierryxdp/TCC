def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    frase = frase.split()
    def retira_pontuacao(frase):
    list.remove(frase, '-')
    list.remove(frase, ",")
    list.remove(frase, ";")
    list.remove(frase, "!")
    list.remove(frase, "?")
    list.remove(frase, ".")
    list.remove(frase, "...")
    
    return frase
    return