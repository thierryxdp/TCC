def lingua_p(word):
    '''Função que retorna uma mesma palavra "word" 
    traduzida para a língua do P.
    word=str->str'''
    str.lower(word)
    x = list(word)
    y = ''
    w = 0
    while w < len(x):
        if 'a' == x[w]:
            y = y + x[w] + 'pa'
            
        elif 'ã' == x[w]:
            y = y + x[w] + 'pã'
            
        elif 'á' == x[w]:
            y = y + x[w] + 'pá'
            
        elif 'â' == x[w]:
            y = y + x[w] + 'pâ'
            
        elif 'e' == x[w]:
            y = y + x[w] + 'pe'
            
        elif 'é' == x[w]:
            y = y + x[w] + 'pé'
            
        elif 'ê' == x[w]:
            y = y + x[w] + 'pê'
            
        elif 'i' == x[w]:
            y = y + x[w] + 'pi'
        
        elif 'í' == x[w]:
            y = y + x[w] + 'pí'

        elif 'o' == x[w]:
            y = y + x[w] + 'po'
            
        elif 'ó' == x[w]:
            y = y + x[w] + 'pó'
            
        elif 'ô' == x[w]:
            y = y + x[w] + 'pô'
            
        elif 'õ' == x[w]:
            y = y + x[w] + 'põ'

        elif 'u' == x[w]:
            y = y + x[w] + 'pu'
            
        elif 'ú' == x[w]:
            y = y + x[w] + 'pú'

        else:
            y = y + x[w]

        w = w + 1
    return y