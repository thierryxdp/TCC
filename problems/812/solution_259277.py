def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a mesma, porém sem os caracteres de pontuação.
    string -> string. """
    
    s = "string. With. Punctuation?"

	punct = string.punctuation
	for c in punct:
    	s = s.replace(c, "")
	print(s)