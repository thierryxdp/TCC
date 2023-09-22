def lingua_p(palavra):
    '''função que recebe uma palavra como parâmetro e retorna esta mesma palavra 
    agora traduzida para a lingua do P e toda em minúscula.
    str - str'''
    
    palavranova = palavra
    i = 0
    for letra in "AEIOUaeiouáéíóúÁÉÍÓÚ":
        palavranova = palavranova.replace(letra, letra+"p"+letra)
	return palavranova