def inverte(frase):
    '''Funcao recebe uma frase e retorna a mesma frase, porem, ivertida, sem nenhuma pontuacao e com letras minusculas
string - > string'''
    removPonto = substitui(frase)
    return str.join(' ',str.split(removPonto)[-1::-1])