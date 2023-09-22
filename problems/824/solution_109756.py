def uppCons(frase):
    '''função que receba como entrada uma frase e retorne a frase com todas
    as suas consoantes maiusculas. Os demais caracterem permanecem iguais.
    str -> str'''
    frasenova = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = frase.upper()
        else:
            frase[i] 
            
        frasenova += frase[i]
        i += 1
    return frasenova