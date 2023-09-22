def lingua_p(palavra):
    '''Função que recebe uma str(palavra) em português;
retorna esta mesma str traduzida para língua do p.
Após cada vogal, uma sequência de p+vogal é inserida.
str->str''' 
    p1 = ['']
    i = 0
    vogais = 'aeiou'
    palavra.split()
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            p1.append(palavra[i]+'p'+palavra[i])
        elif palavra[i] not in vogais:
            p1.append(palavra[i])
        
    return ''.join(p1)