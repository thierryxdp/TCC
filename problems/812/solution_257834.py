def retira_pontuacao(x):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuacao sao substituidos por espaco
    str -> str'''
    acentos=('!','.',',',':',';','-','?')
    aa=str.replace(x,'!',' ')
    aa=sre.replace(aa,'.',' ')
    return aa