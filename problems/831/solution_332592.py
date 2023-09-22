def lingua_p(texto):
    '''retorna uma string com as vogais que apareceram em um texto,
    na mesma sequencia que apareceram
    str->str'''
    
    traducao=""
    for letra in texto:
        if letra in 'AEIOUaeiou':
            traducao=traducao+letra+"p"+letra
	for conso in texto:
        if conso in 'bcdfghjklmnpqrstvxywzç':
            conso=conso+letra
    return (traducao+letra)