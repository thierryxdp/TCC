def retira_pontuacao(texto):
    if texto.count('!')>0:
        return texto.replace(texto.replace('.','') and '!','')

    if texto.count('.')>0 and texto.count(',') == 0 and texto.count('!') == 0 and texto.count('?') == 0:
        return texto.replace('.','')
    
    if texto.count('.')>0 and texto.count(',')>0:
        return texto.replace(texto.replace('.') and ',','')