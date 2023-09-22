def lingua_p(palavra): 
    '''funçao que adiciona linguagem p após uma vogal adicionando "P"+vogal''' 
    '''str->str'''
    P=''
    for letra in palavra: 
        P+= letra
        if letra in 'aáãàâéêeíîioóõôúu' :
            P+= 'p'+letra 
    return P