# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Entrada:
    	É fornecido uma string s ---> str
    Saída:
    	Retorna a string com # no início, meio e final --->str
    '''
    
    num = round((len(s)/2) - 0.4)
    
    return '#' + s[0:num] + '#' + s[num:] + '#'