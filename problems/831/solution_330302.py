def lingua_p(palavra):
    '''Função que recebe um palavra (em português) como entrada e retorna esta mesma
    palavra traduzida para língua do P. Uma palavra é traduzida para lingua do P quando,
    após cada vogal da palavra original, é inserida a seqência de letras p mais a vogal
    original; str->str'''
    ocorrencia=0
    vogais='aeiouáéíóúàèìòùãõâêîôû'
    palavra= str.lower(palavra)
    for i in palavra:
        if i in vogais:
            palavra= str.replace(palavra,i,i+'p'+i,ocorrencia)
        ocorrencia+=1
    return palavra