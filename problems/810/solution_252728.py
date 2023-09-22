def retira_pontuacao(frase):
    '''Dada uma frase, retorna outra frase onde todos os caracteres de pontuação tenham sido substituidos 
    por espaço. str-> str''' 
    frase = frase 
    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.replace(frase,'...',' ')
    return frase 

def inverte(frase):
    '''Dada uma frase, retorna outra frase com as mesmas palavras, porém com a ordem invertida 
    str-> str''' 
    L= retira_pontuacao(frase)
    lista=str.split(L)
    lista= list.reverse(lista)
    L=str.join(' ',lista)
    return L