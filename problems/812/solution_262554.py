def retira_pontuacao(frase):
    '''Função que, dada uma frase como entrada, retorna a frase onde todos os
    caracteres de pontuação(incluíndo travessão, vírgula, dois pontos, ponto e
    vírgula, além da pontuação de encerramento de frase) são substituídos por espaço;
    str->str'''
    substitui_ponto= str.replace(frase,'.',' ')
    substitui_exclamacao= str.replace(substitui_ponto,'!',' ')
    substitui_interrogacao= str.replace(substitui_exclamacao,'?',' ')
    substitui_reticencias= str.replace(substitui_interrogacao,'...',' ')
    substitui_virgula= str.replace(substitui_reticencias,',',' ')
    substitui_travessao= str.replace(substitui_virgula,'-',' ')
    substitui_doispontos= str.replace(substitui_travessao,':',' ')
    substitui_pontoevirgula= str.replace(substitui_doispontos,';',' ')
    nova_frase= substitui_pontoevirgula
    return nova_frase