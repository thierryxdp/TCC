def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
  
    f1 = frase.split("."):
   		return ' '.join(f1)
    f2 = frase.split("!"):
    	return ' '.join(f2)
    f3 = frase.split("?"):
    	return ' '.join(f3)
    f4 = frase.split(","):
   		 return ' '.join(f4)
    f5 = frase.split("..."):
   		 return ' '.join(f5)
    f6 = frase.split("-"):
    	return ' '.join(f6)