def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a 
    lingua do p, em minusculas; str -> str'''
    i=0
    x=0
    palavraMin=str.lower(palavra)
    traducao=list(palavraMin)
    traducao2=''
    while i<len(palavra):
        if palavraMin[i] in 'aeiou':
            traducao[i]=(traducao[i]+'p'+traducao[i])
        i=i+1
    while x<len(traducao):
        traducao2+=traducao[i]
        i=i+1
        
    return traducao2