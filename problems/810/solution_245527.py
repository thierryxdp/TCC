def retira_pontuacao(frase):
    '''Função que, dada uma frase como entrada, retorna a frase onde todos os
    caracteres de pontuação(incluíndo travessão, vírgula, dois pontos, ponto e
    vírgula, além da pontuação de encerramento de frase) são substituídos por espaço;
    str->str'''
    substitui_reticencias= str.replace(frase,'...',' ')
    substitui_exclamacao= str.replace(substitui_reticencias,'!',' ')
    substitui_interrogacao= str.replace(substitui_exclamacao,'?',' ')
    substitui_ponto= str.replace(substitui_interrogacao,'.',' ')
    substitui_virgula= str.replace(substitui_ponto,',',' ')
    substitui_travessao= str.replace(substitui_virgula,'-',' ')
    substitui_doispontos= str.replace(substitui_travessao,':',' ')
    substitui_pontoevirgula= str.replace(substitui_doispontos,';',' ')
    nova_frase= substitui_pontoevirgula
    return nova_frase 



def inverte(frase):
    '''Funçao que, dada uma frase como entrada, retorna uma outra frase contendo as mesmas
    palavras da frase de entrada na ordem inversa, sem letra maiúscula e sem pontuação;str->str'''
    frase_sem_pontuacao= retira_pontuacao(frase)
    palavras_separadas= str.split(frase_sem_pontuacao)
    list.reverse(palavras_separadas)
    frase_invertida= str.join(' ',palavras_separadas)
    nova_frase= str.lower(frase_invertida)
    return nova_frase