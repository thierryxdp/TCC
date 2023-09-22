def retira_pontuacao(frase):
    '''Dada uma frase, a função retorna a frase com as pontuações
    substituídas por espaço
    entrada:str
    saída:str'''
    x = str.replace(frase,'-',' ')+str.replace(frase,',',' ')+str.replace(frase,':',',' ')+
    +str.replace(frase,';',' ')
    return x