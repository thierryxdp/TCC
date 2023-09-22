def uppCons (frase):
    '''Função que recebe uma frase e transforma suas consoantes em MAIÚSCULAS mantendo o resto como estava
    str -> str'''

    Frase_final = ''
    letra = 0

    while letra<len(frase):
        #Enquanto  o contador for menor que o tamanho da lista
        
        if frase[letra] in 'BCDFGHJKLMNPQRSTVÇWXZbcdfgjklhçmnpqrstvwxz':
            #Se a letra na frase for uma consoante 
            Frase_final += str.upper(frase[letra])
                #Transforma em maiúscula a consoante

        else:
            Frase_final += frase[letra]
                #caso a letra não for uma consoante ela se manterá como está e será adicionada à lista

        letra += 1

    return Frase_final