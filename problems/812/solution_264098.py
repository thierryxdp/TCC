def retira_pontuacao(texto):
    '''funcao que dado um texto retira e substitui as pontuacoes
por espacos; str -> str'''
    novo_texto = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),':',' '),';',' '),'?',' '),'!',' '),'.',' ')
    return novo_texto