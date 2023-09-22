def retira_pontuacão(frase):
    '''função que dada uma frase retorne a frase onde todos os caracteres de pontuação que foram substituídos sejam retornados
    str->str'''
    
    frase = str.replace(frase,'!',',',' ')
    frase = str.replace(frase,';',',',' ')
    frase = str.replace(frase,';',',',' ')
    frase = str.replace(frase,'.',',',' ')
    frase = str.replace(frase,'-',',',' ')
    frase = str.replace(frase,'?',',',' ')
    frase = str.replace(frase,',',',',' ')
    return frase