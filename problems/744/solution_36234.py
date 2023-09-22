def hashtag(s):
    """Calcula e retorna a expressao da string "x" mais o caracter
"#" no ínico, meio e fim da string "x"; str --> str"""
    return "#"+s[0:(len(s)//2)]+"#"+[(len(s)//2):]+"#"