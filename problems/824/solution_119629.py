# Questão 2

def uppCons (frase):
    ''' Função que recebe um frase e transforma suas consoantes em MAIÚSCULAS
    mantendo o resto como estava'''

    Frase_final = ''
    letra = 0

    while letra<len(frase):
        #enquanto  o contador for menor que o tamanho da lista
        
        if frase[letra] in 'BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz':
            #se a letra na frase for uma consoante
            
            Frase_final = Frase_final + str.upper(frase[letra])
                #Tranforma em maiúsculas as consoantes

        else:
            Frase_final = Frase_final + frase[letra]
                #caso a letra não for uma consoante ela se manterá como está e será adicionada à lista

        letra= letra +1

    return Frase_final