def lingua_p(palavra):
    '''Função que recebe um palavra (em português) como entrada e retorna esta mesma
    palavra traduzida para língua do P. Uma palavra é traduzida para lingua do P quando,
    após cada vogal da palavra original, é inserida a seqência de letras p mais a vogal
    original; str->str'''
    vogais='aeiouáéíóúàèìòùãõâêîôû'
    palavra= str.lower(palavra)
    nova_palavra=''
    for i in palavra:
        if i in vogais:
            i=i+'p'+i
            nova_palavra=nova_palavra+i
        else:
            nova_palavra=nova_palavra+i
    return nova_palavra