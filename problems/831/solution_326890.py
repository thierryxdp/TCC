def lingua_p(palavra):
    '''Funçao que recebe um parametrocomo de uma palavra( em português) e retorna essa mesma 
    palavra traduzida para a lingua do P.'''
    palavra=strlower(palavra)
    palavra_final=''
    vogais='ãaáàeéèiíoóuú'
    
    for i in palavra:
        palavra_final = palavra_final+i
        if i in vogais:
            palavra_final = palavra_final + 'p' + i
            return palavra_final