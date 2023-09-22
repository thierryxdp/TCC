# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Função que retorna uma string com o caractere # no
        início, no meio e no final dela, sendo s a string
        na qual será adicionada o caractere #
    '''
    comprimento = len(s)
    indice_meio = comprimento/2
    
    if (comprimento % 2 == 0):
        return '#' + s[:indice_meio] + '#' + s[indice_meio:] + '#'
    
    else:
        return '#' + s[:int(indice_meio)] + '#' + s[int(indice_meio):] + '#'