def retira_pontuacao(frase):
    '''Dada uma frase, afunção retorna a frase sem os caracteres
    str -> str'''
    palavra = str.replace(frase,'?',' ')
    palavra = str.replace(palavra,'.',' ')
    palavra = str.replace(palavra,',',' ')
    palavra = str.replace(palavra,'!',' ')
    palavra = str.replace(palavra,'-',' ')
    return palavra


def inverte(frase):
    '''...'''
    
    frase = retira_pontuacao(str.lower(frase))
    frase = frase[0:-1]
    
    
    return frase