def retira_pontuacao(s):
    if '!' in s==True:
    	s=str.join('',remove(s,'!'))
        
    if '.' in s==True:
        s=str.join('',str.split(s,'.'))
        
    if ',' in s==True:
        s=str.join('',str.split(s,','))
        
    if ';' in s==True:
        s=str.join('',str.split(s,';'))
        
    if '-' in s==True:
        s=str.join('',str.split(s,'-'))
        
    if '/' in s==True:
        s=str.join('',str.split(s,'/'))
        
    if ':' in s==True:
        s=str.join('',str.split(s,':'))
        
    if '?' in s==True:
        s=str.join('',str.split(s,'?'))
        
    
    return s