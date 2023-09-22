def lingua_p (palavra):
    ''' retorna a palavra na lingua do P; entrada-> palavra
    (em português); str->str '''
    vogais='aeiou'
    y='p'
    for x in vogais:
        for w in palavra:
           	if x == w :
            	palavra= str.replace(palavra,w,x+y+x,1)
        	else:
                palavra=palavra
    return str.lower(palavra)