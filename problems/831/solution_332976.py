def lingua_p(palavra):
    	'''	 Essa funçao acrescenta um p após a vogal de uma palavra e também acrescenta 
        a vogal dessa palavra a sua mesma vogal após o p (o=opo);str->str'''
        palavra2=str.lower(palavra)
        lista=str.split(palavra2)
        lista2=[]
        for letra in lista:
            
            if letra in 'aeiou':
                p = letra+'p'+letra
                list.append(lista2,p)
            else:
                list.append(lista2,letra)
        return lista2