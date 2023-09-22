def lingua_p (palavra):
    ''' retorna a palavra na lingua do P; entrada-> palavra
    (em português); str->str '''
    vogais='aeiou'
    p='p'
    i=0
    for x in vogais:
        #for w in palavra:
        if x == palavra[i] :
            
          	palavra= str.replace(palavra,x,x+p+x,1)
        
        if x != palavra[i] :
            palavra=palavra
        i=i+1	
    return str.lower(palavra)