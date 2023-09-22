def fatorial(numero):
    """Funcao que calcula e retorna a fatorial de um numero dado.
    Entrada: int;
    Saida: int;
    
    Parameter:
    numero: numero a ser feito o fatorial.
    """
	fat_n = 1  
	while (numero > 1):  
  		fat_n = fat_n * numero
  		numero = numero - 1 
    return fat_n