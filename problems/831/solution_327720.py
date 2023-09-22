def lingua_p(palavra):
    '''retorna uma palavra dada com p`s apos as vogais
    str->str'''
    alterado=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeioéúáu':
            p=(palavra[i] + 'p' + palavra[i])
        	alterado+= p
        else:
          	alterado+=palavra[i]
            
    return alterado