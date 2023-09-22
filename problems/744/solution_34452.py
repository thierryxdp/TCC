# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada a string s, retorna a string s com o caractere # no início, no meio e no final dela;
	assinatura: str --> str
    Casos de teste:
    hashtag('ab') == '#a#b#'
    hashtag('abcd') == '#ab#cd#'
    hashtag('abcde') == '#ab#cde#'
    '''
    s = '#' + s[:int(len(s)/2)] + '#' + s[int(len(s)/2):] + '#'
	return s