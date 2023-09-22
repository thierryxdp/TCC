def retira_pontuacao(s):
    if '!' in s==True:
    	s=str.split(s,'!')
        
    if '.' in s==True:
        s=str.split(s,'.')
        
    if ',' in s==True:
        s=str.split(s,',')
        
    if ';' in s==True:
        s=str.split(s,';')
        
    if '-' in s==True:
        s=str.split(s,'-')
        
    if '/' in s==True:
        str.split(s,'/')
        
    if ':' in s==True:
        s=str.split(s,':')
        
    if '?' in s==True:
        s=str.split(s,'?')
        
    
    return str.join("",s)