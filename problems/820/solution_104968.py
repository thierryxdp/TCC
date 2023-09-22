def posLetra(string, letra,num):
	"""Calcula e retorna a posicao da string em que a 
    ocorrencia(num) desejada da letra em uma string esta;
    str,str,int-->int"""
    i=0
    ocorrencia=-1
    while i < len(string):
        if string[i] == letra and ocorrencia == num:
        ocorrencia= str.count(string,letra)
        i=i+1
	return ocorrencia