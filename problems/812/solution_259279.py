import string

def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a mesma, porém sem os caracteres de pontuação.
    string -> string. """
    
    a = frase

	pontuacao = string.punctuation
	for i in pontuacao:
    	a = a.replace(i, "")
	
    return a