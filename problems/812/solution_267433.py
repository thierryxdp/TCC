def retira_pontuacao(frase):
    '''Dada uma frase, retira todos os caracteres de
    pontuação ('-',',',':',';','.','!','...','?')
    assinatura: str -> str '''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    return frase