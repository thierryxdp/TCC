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
import.retira_pontuacao
def inverte (frase):
    '''c'''
    tarefa= retira_pontuacao.retira_pontuacao(frase)
    frase=str.lower(frase)
    frase_invert=frase[::-1]
    return frase_invert