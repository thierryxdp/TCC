def retira_pontuacao (frase):
    '''Dado uma frase, a função deve retorna a frase 
    onde todas as pontuações foram substituídas por espaços;
    str -> str'''
    frase1=(str.replace(frase,'!',' '))
    frase2=(str.replace(frase1,'?',' '))
    frase3=(str.replace(frase2,'...',' '))
    frase4=(str.replace(frase3,'.',' '))
    frase5=(str.replace(frase4,',',' '))
    frase6=(str.replace(frase5,';',' '))
    frase7=(str.replace(frase6,':',' '))
    frase8=(str.replace(frase7,'-',' '))
    return frase8

def inverte (frase):
    '''Dado uma frase, a função deve retornar outra
    frase que contenha as mesmas palavras da primeira frase
    só que na ordem inversa, sem letras maiúsculas e sem
    pontuação;
    str -> str'''
    frase1=(retira_pontuacao(frase))
    frase2=str.lower(frase1)
    lista=str.split(frase2)
    lista.reverse()
    return str.join(' ',lista)