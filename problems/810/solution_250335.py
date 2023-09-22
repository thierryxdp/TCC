def retira_pontuacao(s): 
	s1=str.replace(s,"-"," ")	
	s2=str.replace(s1,","," ")
	s3=str.replace(s2,":"," ")
	s4=str.replace(s3,"."," ")
	s5=str.replace(s4,";"," ")
	s6=str.replace(s5,'?"," ")
	s7=str.replace(s6,"!"," ")                   
	return s7


def inverte(s):
    '''Função que, dada uma frase, retorna outra frase que contenha
    as mesmas palavras da frase original na ordem inversa, sem 
    letras maiúsculas e sem pontuação.
    assinatura: str -> str '''
    ls=str.split(retira_pontuacao(s))
    list.reverse(ls)
    return str.lower(str.join(" ",ls))