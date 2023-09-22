def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    
    frase.split()
    list.remove(frase, '-')
    list.remove(frase, ",")
    list.remove(frase, ";")
    list.remove(frase, "!")
    list.remove(frase, "?")
    list.remove(frase, ".")
    list.remove(frase, "...")
    
    return frase