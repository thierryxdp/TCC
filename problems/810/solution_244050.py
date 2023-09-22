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
    frase = str.replace(frase,'-',' ',t)
    frase = str.replace(frase,',',' ',v)
    frase = str.replace(frase,':',' ',p2)
    frase = str.replace(frase,';',' ',pv)
    frase = str.replace(frase,'.',' ',e1)
    frase = str.replace(frase,'!',' ',e2)
    frase = str.replace(frase,'?',' ',e3)
    frase = str.replace(frase,'...',' ',e4)
	return frase

def inverte(frase):
    '''Esta função inverte a ordem das palavras de uma dada frase.
    Instruções: Digite a frase entre aspas
    str -> str'''
    frase = retira_pontuacao(frase)
    lista = list(str.split(frase,' '))
    list.reverse(lista)
    x = str.join(' ', lista)    
    return x