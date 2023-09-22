def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço; str->str"""
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    return frase
def inverte(frase2):
    """Função que, dada uma frase, retorna uma outra frase que contém as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação; str->str"""
     frase2 = retira_pontuacao(frase2)
    frase2 = str.split(frase2)
    list.reverse(frase2)
    return str.lower(str.join(' ',frase2))