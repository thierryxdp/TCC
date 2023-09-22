def retira_pontuacao(frase):
    """Essa Função dada uma frase, ela retorna a frase sem caracteres de pontuacao;
    Recebe uma fras;
    Retorna a frase sem caracteres de pontuacao.
    string -> string"""
    f = frase.split('-')
    frase = ' '.join(f)
    f = frase.split(',')
    frase = ' '.join(f)
    f = frase.split(':')
    frase = ' '.join(f)
    f = frase.split('.')
    frase = ' '.join(f)
    f = frase.split(';')
    frase = ' '.join(f)
    f = frase.split('?')
    frase = ' '.join(f)
    f = frase.split('!')
    frase = ' '.join(f)
    
    return frase

def inverte (frase):
    '''Essa função dada uma frase retorna uma outra fase invertida e sem pontuação;
    Recebe uma frase;
    Retorna uma outra fase invertida e sem pontuação.
    string -> string'''
    f = frase.split() 
    list.reverse(f)
    frase = ' '.join(f)
    frase2 = retira_pontuacao(frase)
    f2 = frase2.lower()
	return f2