def lingua_p(palavra):
    ''' traduz uma palavra para a língua do P , que consiste em , após cada vogal da 
    palavra original, inserir-se a sequência de letras 'p' mais a vogal original
    (além disso , a palavra na língua do P está sempre em letras minúsculas);
    str->str'''
    palavra=list(palavra)
    i=0
    while i<len(palavra):
        if palavra[i] in 'aeiou':
            palavra=list.insert(palavra,i+1,'p')
            palavra=list.insert(palavra,i+2,palavra[i])
        i+=1
    return str(palavra)