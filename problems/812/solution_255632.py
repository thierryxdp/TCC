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
    return a