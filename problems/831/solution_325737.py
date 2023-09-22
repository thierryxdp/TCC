def lingua_p(string):
    str.lower(string)
    for letra in string:
    	if letra in 'aeiouáéóúàã':
            string=str.replace(string,letra,letra+"p"+letra)
    return string