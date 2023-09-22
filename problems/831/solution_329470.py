def lingua_p(palavra):
    '''funcao que dada uma frase, sendo esta em portugues, e retorna ela na lingua do P, a qual a letra p vem entre as vogais(duplicadas);
       str-> str'''
    palavratraduzida=''
    for letra in range(len(palavra)):
        if letra in 'aeiou':
            palavratraduzida= palavratraduzida+ palavratraduzida[letra]+ 'p'+palavratraduzida[letra]
        else:
            palavratraduzida= palavratraduzida+palavratraduzida[letra]
    return palavratraduzida