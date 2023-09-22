def qtd_divisores(num):
    lista_num = []
    for div in range(1, num//2+1):
        if num % div == 0: 
            lista_num.append(div)
	return f'O número {num} tem {len(lista_num)+1} divisores.'
#Atribui uma lista a variavel lista_num
#O for me diz que, para div dentro do range de 1, parametro num//2+1