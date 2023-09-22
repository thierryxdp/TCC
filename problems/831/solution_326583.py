def lingua_p(palavra):
    palavra=str.lower(palavra)
    pf=''
    vogais='AEIOUaeiou'
    for i in palavra:
        pf+=i
        if i in vogais:
            v=i+'p'+i
            palavra=str.replace(palavra,i,v)
        
    return palavra