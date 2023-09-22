def retira_pontuacao(frase):
    '''c'''
    resposta=''
    caract_pont=('.','!','?',',',':',';')
    if ('.'and ',') in frase:
        resposta=str.replace(frase,'.',' ')
        resposta=str.replace(resposta,',',' ')
        return resposta
    if '.' in frase:
        return resposta+str.replace(frase,'.',' ')
    if '!' in frase:
        return resposta+str.replace(frase,'!',' ')
    if '?' in frase:
        return resposta+str.replace(frase,'?',' ')
    if ',' in frase:
        return resposta+str.replace(frase,',',' ')
    if ':' in frase:
        return resposta+str.replace(frase,':',' ')
    if ';' in frase:
        return resposta+str.replace(frase,';',' ')