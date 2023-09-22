def retira_pontuacao(frase): 
    """funcao retorna a frase dada modificada com espaços nos lugares dos cracateres de pontuacao;
       str->str"""
    frase.replace ('-',' ')
    frase=frase.replace ('-',' ')
    frase.replace(',',' ')
    frase=frase.replace(',',' ')
    frase.replace(';',' ')
    frase=frase.replace(';',' ')
    frase.replace(':',' ')
    frase=frase.replace(':',' ')
    frase.replace(frase[-1],' ')
    frase=frase.replace(frase[-1],' ')
    return frase



def inverte(frase): 
    """funcao que dada uma frase retorna a frase modificada com a ordem inversa, sem letras maisculas e sem a pontuacao;
       str->str"""
    retira_pontuacao(frase)
    frase=retira_pontuacao(frase)
    frase.lower()
    frase=frase.lower()
    frase=(frase.split())
    lista=(frase.split())
    (lista.reverse())
    return " ".join(lista)