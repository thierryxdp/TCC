def retira_pontuacao(texto):
    '''Função que retira todos os caracteres de pontuação.
    str->str'''
    texto1=''
    
    if '!' in texto:
        texto1+= str.replace(texto,'!',' ')
    if ',' in texto:
        texto1+= str.replace(texto,',',' ')
        return texto1