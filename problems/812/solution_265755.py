def retira_pontuacao(frase):
    """ Dada uma frase retorna a mesma frase sem pontuação
    	entrada string -> saida string"""
    frase = re.sub(r'[^\w\s]','',frase)
  
    
    return frase