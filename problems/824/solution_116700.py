def uppCons(frase):
    #função que entra uma frase e retorna a frase com todas consoantes em maiúsculas
    return ''. join(caractere.upper() if caractere in 'bcçdfghjklmnpqrstvxwyz' else caractere for caractere in frase)