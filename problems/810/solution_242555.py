def retira_pontuacao(frase):
    """funcao que, dada uma frase, retorna essa frase sem qualquer caractere de pontuaçao. Todos esses caracteres serao substituidos por espaço
    str--->str"""
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    return frase

def inverte(frase):
    """ funcao que, dada uma frase, retorna as palavras dessa frase na ordem inversa, sem letras maiusculas e sem pontuacao
    str--->str"""
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    frase=str.partition(frase)
    frase=list.reverse(frase)
    return frase