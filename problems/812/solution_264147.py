def retira_pontuacao(frase):
    '''Função que retorna a mesma frase onde todos os tipos
de pontuação são trocados por espaço;
	str -> str'''
    f=str.replace(frase,'-',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,':',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'!',' ')
    f=str.replace(f,'?',' ')
    return f