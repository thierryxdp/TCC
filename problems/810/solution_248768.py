def retira_pontuacao(frase):
    '''função que dada uma frase(em str) retorna a frase com 
    todos os caracteres de pontuação(.,!,?,,,-,:,;) substitu-
    idos por espaço;str->str'''
    resposta=''
    resposta=str.replace(frase,'.',' ')
    resposta=str.replace(resposta,'!',' ')
    resposta=str.replace(resposta,'?',' ')
    resposta=str.replace(resposta,',',' ')
    resposta=str.replace(resposta,'-',' ')
    resposta=str.replace(resposta,':',' ')
    resposta=str.replace(resposta,';',' ')
    return resposta
def inverte (frase):
    '''c'''
    frase= retira_pontuacao(frase)
    frase=str.lower(frase)
    frase=str.partition(frase,' ')
    frase2=frase[2]
    frase=frase[0]
    return frase2[::-1]+frase[0]