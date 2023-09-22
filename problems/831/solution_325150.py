def lingua_p(palavra):
    '''função que a partir de uma string, retorna a mesma na "língua do P", acrescendando a letra após cada vogal; str -> str'''
    
    nova = ''
    for i in palavra:
        if i not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            nova = nova+i
        if i in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            nova = nova+i+'p'+i
    return nova