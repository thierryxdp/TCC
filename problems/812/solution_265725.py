def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    frase.remove(frase, "-")
    frase.remove(frase, ",")
    frase.remove(frase, ";")
    frase.remove(frase, "!")
    frase.remove(frase, "?")
    frase.remove(frase, ".")
    frase.remove(frase, "...")
    
    return frase