def primo(num):
    lista=range(2,num)

    for numero in lista:
        if num%numero==0:
            return False
       
   	return True