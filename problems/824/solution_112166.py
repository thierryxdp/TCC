def verifica_letra(l):
    '''verifica se a letra eh uma consoante minuscula; str -> str'''
    cons_min=['b','c','d','f','g','h','j','k','l','m',
              'n','p','q','r','s','t','v','w','y','z']
    return str.upper(l) if l in cons_min else l
            
def uppCons(frase):
    '''retorna a frase com as consoantes 
    todas maiusculas; str -> str'''
    frase_cons_maiusc = str.join(
        '',
        map(verifica_letra,frase))
    return frase_cons_maiusc