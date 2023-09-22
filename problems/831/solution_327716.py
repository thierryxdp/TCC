def lingua_p(palavra):
    alterado=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            p=(palavra[i] + 'p' + palavra[i])
        	alterado+= p
        else:
          	alterado+=palavra[i]  
   	return alterado