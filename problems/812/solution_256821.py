def retira_pontuacao(frase):
    '''Dada uma frase, a função retorna a frase com as pontuações
    substituídas por espaço
    entrada:str
    saída:str'''
    x = str.count(frase,'!')+str.count(frase,',')+str.count(frase,'.')+str.count(frase,'-')+str.count(frase,';')
    return str.replace(x,' ')