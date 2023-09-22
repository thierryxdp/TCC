def retira_pontuacao(frase):
    '''Dado uma frase, retorna uma frase sem nenhuma pontuação com espaços
    em seu lugar.str -> str'''
    P = ('!','?','...','.','-',',',':',';')
    if P in frase:
        frase = str.replace(frase,"P"," ")
    return frase