def retira_pontuacao (frase):
    '''Função que recebe uma frase (frase) e retorna a mesma
    frase com os caracteres de pontuação substituidos por
    espaço;
    
    '''
    a = frase.replace('.',' ')
    b = a.replace('...',' ')
    c = b.replace('!',' ')
    d = c.replace('?',' ')
    e = d.replace('-',' ')
    f = e.replace(',',' ')
    g = f.replace(':',' ')
    h = g.replace(';',' ')
    return h