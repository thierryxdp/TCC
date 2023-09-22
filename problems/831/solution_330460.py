def lingua_p(palavra):
    '''Recebe como parâmetro uma palavra (em português) e retorne esta mesma
    palavra traduzida para a língua do P.
    str->str
    '''
    palavra.lower()
    aux='aiueoáíúéóâîûêô'
    linguap=''
 
    for x in range(len(palavra)):
        linguap=linguap+palavra[x]
        if palavra[x] in aux:
            linguap=linguap +'p'
            linguap=linguap+palavra[x]
    return linguap