def vogal(x):
    if x in 'aeiou':
    	return True
    else:
        return False

def uppCons(frase):
    i=0
    while i<len(frase):
        if vogal(frase[i])==False:
            str.upper(frase[i])
        i=i+1
    return frase