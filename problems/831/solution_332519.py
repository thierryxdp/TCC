def lingua_p(palavra):
    '''
       Dada uma palavra a função retorna a palavra dada como
       entrada com o a letra p após cada vogal e a vogal 
       depois do p.
       str -> str
    '''
    palavra_final = ''
    for i in range(palavra):
        if caractere[i] in 'aeiou':
            palavra_final = str.replace(palavra, caractere, caractere + 'p' + caractere)
    return palavra_final