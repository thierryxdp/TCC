def retira_pontuacao(x:str):
    if '.'or'!'or'?'or'-'or','or';'or':' in x:
        return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x,'.',' '),'!',' '),'?',' '),'-',' '),',',' '),':',' '),';',' ')
    else:
        return x