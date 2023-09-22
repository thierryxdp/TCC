def lingua_p(palavra):
    	'''	 Essa funçao acrescenta um p após a vogal de uma palavra e também acrescenta 
        a vogal dessa palavra a sua mesma vogal após o p (o=opo);str->str'''
        palavra2=str.lower(palavra)
        lista=[]
        for letra in palavra2:
            lista.append(letra)
        lista2=[]
        for letra in lista:
            if letra in 'aeiou':
                p = letra+'p'+letra
                lista2.append(p)
            else:
                lista2.append(letra)
        return str.join('',lista2)