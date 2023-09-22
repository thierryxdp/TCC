def lingua_p(texto):
    '''retorna uma string com as vogais que apareceram em um texto,
    na mesma sequencia que apareceram
    str->str'''
    
    vogais=""
    consoantes=""
    for letra in texto:
        if letra in 'AEIOUaeiou':
            vogais=vogais+letra+"p"+letra

        if letra in 'bcdfghjklmnpqrstvxywzç':
            consoantes=consoantes+letra
    return (vogais, consoantes)