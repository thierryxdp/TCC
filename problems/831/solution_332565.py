def lingua_p(texto):
    '''retorna uma string com as vogais que apareceram em um texto,
    na mesma sequencia que apareceram
    str->str'''
    
    vogais=""
    for letra in texto:
        if letra in 'AEIOUaeiou':
            vogais=vogais+"p"+letra
    return vogais