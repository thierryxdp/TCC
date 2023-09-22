def lingua_p (palavra):
    ''''funcao que recebe como parâmetro uma palavra 
    e retorna esta mesma palavra traduzida para a 
    língua do P
    str-->str'''
    minusculo = palavra.lower()
    nova_palavra = ' '
    vogais = 'aeiouãáéíóú'
    for p in minusculo:
        nova_palavra += p
        if p in vogais: 
            nova_palavra += 'p' + p
    return nova_palavra