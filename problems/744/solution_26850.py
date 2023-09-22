# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Para por uma #no inicio, meio e fim a sua string, digite;
    str->str"""
    if len(s)==2:
        return '#'+s[0:1]*2+'#'+s[1:2]*2+'#'
    
    elif len(s)==3:
        return '#'+s[0:1]*2'#'+s[1:3]*2+'#'
	
    elif len(s)==4:
        return '#'+s[0:2]*2'#'+s[2:4]*2+'#'
    
    elif len(s)==5:
        return '#'+s[0:2]*2'#'+s[2:5]*2+'#'
    
    elif len(s)==6:
        return '#'+s[0:3]*2'#'+s[3:6]*2+'#'
    
    elif len(s)==7:
        return '#'+s[0:3]*2'#'+s[3:7]*2+'#'