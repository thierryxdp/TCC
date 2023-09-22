def lingua_p(palavra):
    '''retorna a palavra fornecida traduzida para a 
    lingua do p, em minusculas; str -> str'''
    palavraMin=list(str.lower(palavra))
    traducao=''
    i=0
    while i<len(palavra):
        if palavraMin[i]in'aeiouAEIOU':
            list.replace(palavraMin,i,'p')
            
        i=i+1
    return palavraMin