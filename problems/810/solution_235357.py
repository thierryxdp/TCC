def retira_pontuação(frase):
    '''Função que dada uma frase com as seguintes pontuações !, ?, ., ',', :, ; e -
    substitui cada uma por espaço(' ') e escreve a frase retornada sem essescaracteres
    str->str'''
    frase0=frase
    frase1=str.replace(frase0 ,'.', ' ')
    frase2=str.replace(frase1 ,'-', ' ')
    frase3=str.replace(frase2 ,':', ' ')
    frase4=str.replace(frase3 ,';', ' ')
    frase5=str.replace(frase4 ,',', ' ')
    frase6=str.replace(frase5 ,'?', ' ')
    frase7=str.replace(frase6 ,'!', ' ')
    return frase7
def inverte(frase):
    '''Função que ao receber uma frase retorna essa frase invertida, com
letras minúsculas e sem todas as suas pontuações
str->str'''
    f0=str.lower(retira_pontuação(frase))
    f1=str.split(f0)
    return ' '.join(f1[::-1])