# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Recebe uma string e retorna essa string com "#" no começo, meio e final'''
    meio = (len(s)/ 2)
    retorno = '#' + s[:int(meio)] + '#' + s[int(meio):] + '#'
    
    return retorno