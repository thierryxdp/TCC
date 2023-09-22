def retira_pontuacao(frase):
    '''Esta função substitui a pontuação da frase por espaços.
    Instruções: Digite a frase entre aspas
    str -> str'''
    t = str.count(frase,'-')
    v = str.count(frase,',')
    p2 = str.count(frase,':')
    pv = str.count(frase,';')
    e1 = str.count(frase,'.')
    e2 = str.count(frase,'!')
    e3 = str.count(frase,'?')
    e4 = str.count(frase,'...')
#Substituições
    x= str.replace(frase,'-',' ',t)
	return x