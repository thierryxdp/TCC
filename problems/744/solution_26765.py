# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna uma string onde é adicionado o # no começo, meio e final da string
    	str-> str'''
    return "#"+ s[0:len(s)/2]+ "#" + s[len(s)/2+1:]+ "#"