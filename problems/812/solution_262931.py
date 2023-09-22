def retira_pontuacao(frase):
    '''Dada uma frase retornará a mesma frase, mas sem pontuação alguma.(str=>str)'''

    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,':',' ')

    return frase