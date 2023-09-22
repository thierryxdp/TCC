def lingua_p(palavra):
    '''Função que dada uma palavra, retorna a mesma palavra traduzida para a língua do P. Quando após cada vogal da palavra, é inserida a letra ´p´;
       str->str'''
     lingua= '' 
    for i in palavra:
    	if i in 'aeiouáéúí':
            lingua= lingua + l + 'p' + l
        else: 
            lingua=lingua + l
    return lingua