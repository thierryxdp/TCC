def lingua_p(palavra):
    alterado=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeioéúáu':
            p=(palavra[i] + 'p' + palavra[i])
        	alterado+= p
        else:
          	alterado+=palavra[i]
            
    return alterado