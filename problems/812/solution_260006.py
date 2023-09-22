def retira_pontuacao(frase):
    """retorna a frase dada anteriormente, sem nenhum tipo de pontuacao; str-> str"""
	filtro= frase.replace(';',' ')
    filtro2= filtro.replace('-',' ')
    filtro3= filtro2.replace('!',' ')
    filtro4= filtro3.replace('?',' ')
    filtro5= filtro4.replace('.',' ')
    filtro6= filtro5.replace(':',' ')
    filtro7= filtro6.replace(',',' ')
    
    return filtro7