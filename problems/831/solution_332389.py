def lingua_p(palavra):
    '''
    funçao que recebe uma palavra em portugues e a retorna na lingua do p, que é
    inserir o p apos a vogal mais a vogal, ignorando a difernça entre maiusculas e
    minusculas
    string -> string
    '''
    p = ''
    mini = str.lower(palavra)
    for i in range(len(mini)):
        if i in 'aeiou':
            p = p + i +'p'+i
        else:
            p = p + i
    return p