def retira_pontuacao(frase):
    '''c'''
    resposta=''
    caract_pont=('.','!','?',',',':',';')
    if '.'and'!'and'?'and','and':'and';' in frase:
        resposta=str.replace(frase,'.',' ')
        resposta=resposta+str.replace(frase,',',' ')
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