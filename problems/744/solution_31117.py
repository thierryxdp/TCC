# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Função que retorna uma string com o caractere # no
        início, no meio e no final dela, sendo s a string
        na qual será adicionada o caractere #
        : param s: str
        : return: str
    '''
    indice_meio = len(s)/2
    
    return '#' + s[:int(indice_meio)] + '#' + s[int(indice_meio):] + '#'