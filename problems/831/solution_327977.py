def lingua_p(palavra):
    '''Função que recebe uma str(palavra) em português;
retorna esta mesma str traduzida para língua do p.
Após cada vogal, uma sequência de p+vogal é inserida.
str->str'''
    p1 = ['']
    i = 0
    palavra.split()
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            p1.append(palavra[i-1]+palavra[i]+'p'+palavra[i])
            
    return ''.join(p1)