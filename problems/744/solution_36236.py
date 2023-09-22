def hashtag(s):
    """Calcula e retorna a expressao da string "x" mais o caracter
"#" no ínico, meio e fim da string "x"; str --> str"""
    p1=(len(s)//2)
    return "#"+s[0:p1]+"#"+s[p1:]+"#"