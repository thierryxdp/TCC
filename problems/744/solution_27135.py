# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''A funcao revebe uma string s e retorna essa string modificada pela adição do
caractere "#" no início, no meio e no final dela
	Parametro de entrada: string
    Valor de retorno: string'''
    meio=len(s)//2
    s="#"+s[:meio]+"#"+s[meio:]+"#"
    return s