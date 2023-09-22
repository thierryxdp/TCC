#QUESTÃO 3
def retira_pontuacao(frase):
    '''Dada uma frase, retira todos os caracteres de pontuação
    ('-',',',':',';','.','!','...','?')
    assinatura: str -> str '''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    return frase 

#QUESTÃO 4
def inverte(frase):
    '''Dada uma frase, retira a ponutação, torna todas as letras minúsculas
    e inverte a ordem das palavras
    assinatura: str -> str '''

    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    palavras = str.split(frase)
    list.reverse(palavras)
    
    return ' '.join(palavras)