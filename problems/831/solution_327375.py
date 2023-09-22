def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a 
    lingua do p, em minusculas; str -> str'''
    i=0
    palavraMin=str.lower(palavra)
    traducao=list(palavraMin)
    while i<len(palavra):
        if palavraMin[i] in 'aeiou':
            traducao[i]=(traducao[i]+'p'+traducao[i])
        i=i+1
    return str.join(traducao,' ')