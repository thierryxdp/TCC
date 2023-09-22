def hashtags(s):
    """Calcula e retorna a expressao da
string "x" mais o caracter"#" no ínico,
meio e fim da string "x"; str --> str"""
    p1=(floor(len(s)/2)
    y1=s[0:p1]
    y2=s[p1:]
    return "#"+y1+"#"+y2+"#"