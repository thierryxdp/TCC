def retira_pontuacao(frase):
    f=str.replace(frase,'-',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'!',' ')
    f=str.replace(f,'?',' ')
    return f
def inverte(frase):
    '''Função que retorna a frase de entrada sem pontuação,
sem letra maiúscula e na ordem inversa;
	str -> str'''
    retira_pontuacao(frase)
    f=str.lower(frase)
    f=str.split(f)
    f.reverse()
    f=str.join(' ',f)
    return f