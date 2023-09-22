def retira_pontuacao(frase):
    '''c'''
    caract_pont=('.','!','?',',',':',';')
    resposta=''
    if '.' in frase:
        resposta+str.replace(frase,'.',' ')
    if '!' in frase:
        resposta+str.replace(frase,'!',' ')
    if '?' in frase:
        resposta+str.replace(frase,'?',' ')
    if ',' in frase:
        resposta+str.replace(frase,',',' ')
    return resposta