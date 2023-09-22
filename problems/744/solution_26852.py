# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Para por uma #no inicio, meio e fim a sua string, digite;
    str->str"""
    if len(s)==2:
        return '#'+s[0:1]+'#'+s[1:2]+'#'
    
    elif len(s)==3:
        return '#'+s[0:1]+'#'+s[1:3]+'#'
	
    elif len(s)==4:
        return '#'+s[0:2]+'#'+s[2:4]+'#'
    
    elif len(s)==5:
        return '#'+s[0:2]+'#'+s[2:5]+'#'
    
    elif len(s)==6:
        return '#'+s[0:3]+'#'+s[3:6]+'#'
    
    elif len(s)==7:
        return '#'+s[0:3]+'#'+s[3:7]+'#'
    
    elif len(s)==8:
        return '#'+s[0:4]'#'+s[4:8]+'#'
    
    elif len(s)==9:
        return '#'+s[0:4]+'#'+s[4:9]+'#'
    
    elif len(s)==10:
        return '#'+s[0:5]+'#'+s[5:10]+'#'
    
    elif len(s)==11:
        return '#'+s[0:5]+'#'+s[5:11]+'#'
    
    elif len(s)==12:
        return '#'+s[0:6]+'#'+s[6:12]+'#'
    
    elif len(s)==14:
        return '#'+s[0:7]+'#'+s[7:14]+'#'