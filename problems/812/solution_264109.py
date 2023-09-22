def retira_pontuacao(frase):
    '''c'''
    caract_pont=('.','!','?',',',':',';')
    resposta=''
    if '.' in frase:
        return resposta+str.replace(frase,'.',' ')
    if '!' in frase:
        return resposta+str.replace(frase,'!',' ')
    if '?' in frase:
        return resposta+str.replace(frase,'?',' ')
    if ',' in frase:
        return resposta+str.replace(frase,',',' ')