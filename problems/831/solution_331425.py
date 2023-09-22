def lingua_p(palavra):
    '''
    função que recebe uma palavra e retorna essa mesma palavra traduzida na lingua 'p', na qual
    apos a ocorrência de uma vogal, é inserida na sequência a letrap+vogal da palavra original
    resposta ignora maiusculas e minusculas e retorna toda a palavra traduzida minuscula
    str--->str
    '''
    
    i=0
    consoantes='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    
    nova_palavra=''
    for letra in palavra:
        if letra not in consoantes:
            nova_palavra= nova_palavra+(letra+'p'+letra)
        else:
            nova_palavra= nova_palavra+letra
            
    return str.lower(nova_palavra)