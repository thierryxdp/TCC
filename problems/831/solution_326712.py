def linagua_p(palavra):
    '''Ao fornecer uma palavra em português, insere a letra "p" e a vogal 
    original, após cada vogal. Ao final, deve-se retorna a palavra em letras minúsculas.

    str -> str'''

    palavra = str.upper(palavra)
    palavra = list(str(palavra))

    palavra_tratada = []
    
    for letra in range(len(palavra)):
        list.append(palavra_tratada, palavra[letra])
        if palavra[letra] not in 'BCDFGHJKLMNPQRSTVWXYZÇ':
           list.append(palavra_tratada,'P'+palavra[letra])
           
    palavra_tratada = str.join('',palavra_tratada)  
 
    return str.lower(palavra_tratada)