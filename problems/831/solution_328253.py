def lingua_p(s):
    '''Traduz um string para a lingua do P'''
    string=''
    for i in s:
        if i in 'aeiouãáéíóú':
            string+=i+'p'+i
        else:
            string+=i
    return string.lower()