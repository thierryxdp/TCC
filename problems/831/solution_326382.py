def lingua_p(palavra):
    a=str.lower(palavra)
    palavra_p=''
    
    for i in a:
        if i in 'aeiou':
            i='p'+i+'p'
            
        palavra_p+=i
        
    return palavra_p