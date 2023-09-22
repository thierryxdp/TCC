def retira_pontuacao(frase : str)->str:
    """ Dada uma frase retorna essa frase, mas sem pontuação."""

    frase_limpa = str.replace(str.replace(str.replace(str.replace
                  (str.replace(str.replace(str.replace
                  (str.replace(frase,'...',' '),',',' '),';',' ')
                 ,':',' '),'-',' '),'?',' '),'!',' '),'.',' ')
    
    return frase_limpa


def inverte(frase : str)->str:
    
    """Dada uma frase retorna outra frase contendo as
    mesmas palavras da frase fornecida, mas na ordem inversa."""

    min_e_limpa = retira_pontuação(str.lower(frase))
    
    lista = (str.split(min_e_limpa))
    lista_invertida = lista[-1:(-len(lista)-1):-1]
    
    return str.join(" ",lista_invertida)