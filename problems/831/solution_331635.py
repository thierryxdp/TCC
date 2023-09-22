def lingua_p(palavra):
    '''função que recebe como parâmetro uma palavra (em português) e retorna ela traduzida para a língua do P,que é quando após cada vogal da palavra original, é insirida a sequência de letras 'p' mais a vogal original; str -> str'''
    i=0
    palavra=str.lower(palavra)
    for d in palavra:
        if d in 'AEIOUÁÉÍÓÚÃÕáéíóúãõaeiou':
            palavra=list(palavra)
            list.insert(palavra,i+1,'p'+d)
            i=i+2
        else:
            i=i+1
    palavra=(' '.join(palavra))
    palavra=str.replace(palavra,' ','')
    return palavra