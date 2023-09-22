def retira_pontuacao(frase):
    '''Dado uma string frase, retorne uma string sem pontos de pontuação;
    string -> string'''
    a=str.replace(frase,'/',' ')
    a=str.replace(a,',',' ')
    a=str.replace(a,':',' ')
    a=str.replace(a,';',' ')
    a=str.replace(a,'.',' ')
    a=str.replace(a,'!',' ')
    a=str.replace(a,'?',' ')
    a=str.replace(a,'-',' ')
    return a
def inverte(frase):
    '''Dado uma frase, retorne ela invertida; string -> string'''
    a=retira_pontuacao(frase)
    a=str.lower(a)
    a=str.split(a)
    a=a[::-1]
    a=str.join(' ',a)
    return a