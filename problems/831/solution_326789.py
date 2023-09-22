def lingua_p (palavra):
    """Recebe uma palavra e retorna ela traduzida para a 
    língua do P, ou seja, a vogal seguida de p e a vogal
    repetida.
    str -> str"""
    nova_palavra = str.lower(palavra)
    p = []
    for i in range(len(palavra)):
        if nova_palavra[i] in 'aeiou':
            p += (nova_palavra[i]+'p'+nova_palavra[i])	        
        else:	           
            p += nova_palavra[i]
    return str.join('', p)