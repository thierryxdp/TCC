def retira_pontuacao(frase):
    resposta1=str.replace(frase,'-',' ')
    resposta2=str.replace(resposta1,',',' ')
    resposta3=str.replace(resposta2,':',' ')
    resposta4=str.replace(resposta3,';',' ')
    resposta5=str.replace(resposta4,'.',' ')
    resposta6=str.replace(resposta5,'!',' ')
    resposta7=str.replace(resposta6,'?',' ')
    resposta8=str.replace(resposta7,'...',' ')
    return resposta8



def inverte(frase):
    alterada=retira_pontuacao(frase)
    resposta=str.lower(alterada)
    respostacorreta=str.split(resposta)
    list.reverse()
    return respostacorreta