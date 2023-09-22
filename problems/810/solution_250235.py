def inverte(s):
    """Função que quando dada uma frase, retorna outra frase , porém com todas as palavras sendo letras minúsculas, escrita ao contrário e sem pontuações.
assinatura: str -> str
testes:
inverte("Maria Eduarda, licencianda em Matemática. Estudante de computação. Tomara que seja aprovada!") == 'aprovada seja que tomara computação de estudante matemática em licencianda eduarda maria'
inverte("Quer ir ao pagode? Não conseguirei, tenho trabalhos a fazer!") == 'fazer a trabalhos tenho conseguirei não pagode ao ir quer'
"""
    
    str.replace(s,".", ' ')
    s2 = str.replace(s,".", ' ')
    str.replace(s2,"!", ' ')
    s3 = str.replace(s2,"!", ' ')
    str.replace(s3,"?",' ')
    s4 = str.replace(s3,"?", ' ')
    str.replace(s4,"-", ' ')
    s5 = str.replace(s4,"-", ' ')
    str.replace(s5,",", ' ')
    s6 = str.replace(s5,",", ' ')
    str.replace(s6,";",' ')
    s7 = str.replace(s6,";", ' ')
    str.replace(s7,"...", ' ')
    s8 = str.replace(s7,"...", ' ')
    str.replace(s8,":", ' ')
    s9 = str.replace(s8,":", ' ')
    str.split(s9)
    ls = str.split(s9)
    list.reverse(ls)
    str.join(" ",ls)
    ls2 = str.join(" ",ls)
    return str.lower(ls2)