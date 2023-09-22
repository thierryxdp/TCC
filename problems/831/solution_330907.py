def lingua_p(palavra):
    ''' traduz uma palavra para a língua do P , que consiste em , após cada vogal da 
    palavra original, inserir-se a sequência de letras 'p' mais a vogal original
    (além disso , a palavra na língua do P está sempre em letras minúsculas);
    str->str'''
    palavra=list(palavra)
    i=0
    nova_palavra=palavra
    while i<len(palavra):
        if palavra[i] in 'aeiou':
            list.insert(nova_palavra,i+1,'p')
            list.insert(nova_palavra,i+2,palavra[i])
        i+=1
    return str(nova_palavra)