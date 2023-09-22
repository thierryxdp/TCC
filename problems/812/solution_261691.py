def retira_pontuacao(frase):
    '''Funcao que, dada uma frase, retorna essa frase com todos os caracteres de pontuacao (travessao, virgula, dois pontos, ponto e virgula e ponto final) por espaco; str -> str'''
    frase=str.replace(frase,',','')
    frase=str.replace(frase,'.','')
    frase=str.replace(texto,'—','')
    frase=str.replace(texto,':','')
    frase=str.replace(texto,';','')
    return frase