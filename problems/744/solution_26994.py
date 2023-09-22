def hashtag(s):
    """Função que, ao receber uma string, retorna ela com o caractere "#" no início, no meio e no final dela
       str->str"""
       meio=len(s)//2
    return "#"+s[0:meio]+"#"+s[meio:]+"#"