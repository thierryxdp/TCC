# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Função recebe uma string(s) e retorna uma outra 
        string com o símbolo # no início, no meio e no final
        str -> str
        
    '''
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'