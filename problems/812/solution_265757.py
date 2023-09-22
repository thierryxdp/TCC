def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    import re
    frase = ''.join([i for i in frase if i not in string.punctuation])
  
    
    return frase