# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    funcao criada para colocar o caractere # no inicio, meio e final de uma string
    parametros:
    s: string
    saida: 
    string com o # no inicio, meio e fim
    '''
	s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return (s)