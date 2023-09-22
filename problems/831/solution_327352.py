def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a 
    lingua do p, em minusculas; str -> str'''
    traduzida=''
    i=0
    minuscula=str.lower(palavra)
    while i<len(minuscula):
        if minuscula[i]in'aeiou':
            traduzida=traduzida[:i+1]+(minuscula.replace(minuscula[i],(minuscula[i]+'p'+minuscula[i]))[i:])
    		
        i=i+1
    return traduzida