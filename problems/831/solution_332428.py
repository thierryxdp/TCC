def lingua_p(palavra):
    '''função que recebe uma palavra e retorna a mesma
    traduzida para a lingua do p'''
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nova_palavra = ""
    for i in palavra:
        if i in vogais:
            nova_palavra+=i
            nova_palavra+="p"
            nova_palavra+=i
        else:
            nova_palavra+=i
    return(nova_palavra.lower())