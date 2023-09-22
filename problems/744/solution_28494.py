# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    incere hashtags na string
    parâmetros
    	s:str
    saída
    	sttr
    '''
    comp_s = len(s)
    if comp_s%2==0:
        saida = "#"+s[0:comp_s//2]+"#"+s[comp_s//2: comp_s+1]+"#"
    else:
        saida = "#"+s[0:comp_s//2]+"#"+s[comp_s//2:comp_s+1]+"#"
    return saida