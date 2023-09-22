def uupCons(string):
    """Função que retorna a string com todas as consoantes maiúsculas e o resto
    da string exatamente com estava antes;
    string -> string"""
    i=0
    s=''
    while i<len(string):
        if string[i].lower() != 'a' and string[i].lower() != 'e' and string[i].lower() != 'i' and string[i].lower() != 'o' and string[i].lower() != 'u':
            string.replace(string[i], string[i].upper())
            s+= string[i].upper()
        else:
            s+=string[i]
        i+=1
    return s