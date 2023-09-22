def uppCons(string):
    """Função que retorna a string com todas as consoantes maiúsculas e o resto
    da string exatamente com estava antes;
    string -> string"""
    i=0
    s=''
    while i<len(string):
        if string[i].lower() != 'a' and string[i].lower() != 'e' and string[i].lower() != 'i' 
        and string[i].lower() != 'o' and string[i].lower() != 'u' and string[i].lower() != 'ã' 
        and string[i].lower() != 'é' and string[i].lower() != 'í' and string[i].lower() != 'ó' 
        and string[i].lower() != 'ú':
            string.replace(string[i], string[i].upper())
            s+= string[i].upper()
        else:
            s+=string[i]
        i+=1
    return s  ã ó ú í é