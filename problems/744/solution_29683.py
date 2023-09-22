# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''dada uma str 'rotulo' retorna essa str acrescida do
    caracter '#' no seu inicio, no meio e no final
    entrada: str
    saida: str'''
    rotulo=s
    pt=len(rotulo)//2
    meio_dito='#'+rotulo[0:pt]+'#'
    rotulo=meio_dito+rotulo[pt:]+'#'
    return rotulo