def filtraMultiplos(lista_num, num):
    
    i=0
    is_divisible = []
    while i< len(lista_num):
        if not lista_num[i]%num:
            is_divisible.append(lista_num[i])
        i+=1
  	return is_divisible