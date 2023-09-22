def substitui(frase,letra,i):
    '''Entre com uma string, um caracter e um numero inteiro para retornar
    uma nova string com o caracter na posição do inteiro
    string, char, int -> string'''
	
    num=i
    frase2=frase.replace(frase[num], letra, 1)
  
    return frase2