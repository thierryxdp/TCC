def retira_pontuacao(frase):
    '''recebe e retorna uma frase que todos os caracteres de pontuação foram substituídos por espaço
    str -> str'''
	
    frase=frase.replace('-' , ' ')
	frase=frase.replace(',' , ' ')
	frase=frase.replace(';' , ' ') 
	frase=frase.replace(':' , ' ')
	frase=frase.replace('.' , ' ')
	frase=frase.replace('?' , ' ')
	frase=frase.replace('!' , ' ')
    
    return frase