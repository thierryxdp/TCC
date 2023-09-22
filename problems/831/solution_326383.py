def lingua_p(palavra):
    a=str.lower(palavra)
    palavra_p=''
    
    for i in a:
        if i in 'aeiou':
            i=i+'p'+i
            
        palavra_p+=i
        
    return palavra_p