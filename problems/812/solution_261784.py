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
    
    if e4 >=1:
        e1 = e1 - (e4*3)
    else:
        e1 = e1
#Substituições
    str.replace(frase,'-',' ',t)
    str.replace(frase,',',' ',v)
    str.replace(frase,':',' ',p2)
    str.replace(frase,';',' ',pv)
    str.replace(frase,'.',' ',e1)
    str.replace(frase,'!',' ',e2)
    str.replace(frase,'?',' ',e3)
    str.replace(frase,'...',' ',e4)
	return frase