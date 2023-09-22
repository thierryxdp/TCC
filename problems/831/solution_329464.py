def lingua_p(palavra):
    '''funcao que dada uma frase, sendo esta em portugues, e retorna ela na lingua do P, a qual a letra p vem entre as vogais(duplicadas);
       str-> str'''
    palavratraduzida=''
    for letra in len(range(palavra)):
        if letra in 'aeiou':
            palavratraduzida= palavratraduzida+ letra+ 'p'+letra
        else:
            palavratraduzida= palavratraduzida+letra
    return palavratraduzida