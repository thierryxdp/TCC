def primo(n):
    '''função verifica se um número inteiro dado é primo.int->bool'''
    listadediv=[]
    for x in range(2,n):
        if n%x==0:
            list.append(listadediv,n)
        elif len(listadediv)>=1:
        	return False
    else:
        return True