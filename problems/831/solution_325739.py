def lingua_p(string):
    str.lower(string)
    palavra=''
    for letra in string:
    	if letra in 'aeiouáéóúàâêîôûãõ':
            palavra=palavra+letra+'p'+letra
        else:
            palavra=palavra+letra
    return palavra