def lingua_p(palavra):
    'função que recebe uma palavra(string) e retorna a palavra na língua do p.'
    'após cada vogal da palavra, segue a letra p seguida da vogal original. str->str'
    nova=''
    i=0
    while i<len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            nova+=palavra[i]+'p'+palavra[i]
            i+=1
        else:
            nova+=palavra[i]
            i+=1
    return str.lower(nova)