def lingua_p (palavra):
    ''' retorna a palavra na lingua do P; entrada-> palavra
    (em português); str->str '''
    vogais='aeiou'
    i=0
    y='p'
    for x in vogais:
        while i<= len(palavra):
           	if x == palavra[i]:
            	str.replace(palavra,x,x+y+x)
        		i=i+1    
    return str.lower(palavra)