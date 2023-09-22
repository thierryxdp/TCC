def inverte(s):
    ''' Função que recebe uma frase e retorna a mesma na ordem inversa sem pontuação e letras maiúsculas;string->string'''
    s1=retira(s)
    s2=str.split(s1,' ')
    s4=s2[-1:0:-1]
    s5= str.join(' ',s4)
    s6= str.lower(s5+' '+s2[0])
    return s6