# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna uma string com o caractere # no início, meio e fim da mesma; str -> str'''
    if len(s)==0:
        return s  
    
    elif len(s)==1:
        return '#'+s*2+'#'
    
    elif len(s)==2:
        return s[0:1]*2+s[1:2]*2
    
    elif len(s)==3:
        return s[0:1]*2+s[1:3]*2
	
    elif len(s)==4:
        return s[0:2]*2+s[2:4]*2
    
    elif len(s)==5:
        return s[0:2]*2+s[2:5]*2
    
    elif len(s)==6:
        return str('#')+s[0:3]*2+s[3:6]*2
    
    elif len(s)==7:
        return str('#')+s[0:3]*2+str('#')+s[3:7]*2+str('#')
    elif len(s)==8:
        return s[0:4]*2+s[4:8]*2
    
    elif len(s)==9:
        return s[0:4]*2+s[4:9]*2
    
    elif len(s)==10:
        return s[0:5]*2+s[5:10]*2
    
    elif len(s)==11:
        return s[0:5]*2+s[5:11]*2
    
    elif len(s)==12:
        return s[0:6]*2+s[6:12]*2
    
    elif len(s)==14:
        return s[0:7]*2+s[7:14]*2