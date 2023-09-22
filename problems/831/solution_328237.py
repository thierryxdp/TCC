def lingua_p(palavraemportugues):
    '''funcao que retorna a palavra em portugues para
    a lingua do p; str->str'''
    lista_palavra=[]
    for let in palavraemportugues:
        let=str.lower(let)
        if let in 'aeiouãõáíéúóâêôîû':
            f= let+'p'+let
            list.append(lista_palavra,f)
        else:
            list.append(lista_palavra,let)
    return str.join('',lista_palavra)