def lingua_p(palavra):
    '''
       Dada uma palavra a função retorna a palavra dada como
       entrada com o a letra p após cada vogal e a vogal 
       depois do p.
       str -> str
    '''
    for vogal in palavra:
        palavra_final = ''
        for caractere in palavra:
            if caractere in 'AEIOUaeiou':
                palavra_final = 'p' + caractere in palavra
    return palavra_final