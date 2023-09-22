def retira_pontuacao(frase):
    """ Função que retorna a frase dada como parâmetro, onde todos os caracteres de pontuação tenham sido substituídos por espaço;
        string -> string"""
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'.',' ')
    return frase

def inverte(frase):
    """ Função que dada uma frase retorna uma outra frase que contenha as mesmas palavras de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação;
        string -> string"""
    frase = str.lower(retira_pontuacao(frase))
    frase = str.split(frase,' ')
    frase_invertida = list.reverse(frase)
    frase_invertida = str.join(' ', frase)
    frase_invertida = str.strip(frase_invertida)
    return frase_invertida