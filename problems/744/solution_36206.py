def hashtag(s):
    """Calcula e retorna a expressao da
string "x" mais o caracter"#" no ínico,
meio e fim da string "x"; str --> str"""
    y1=s[0:(floor((len(s)/2))]
    y2=s[(floor((len(s)/2)):]
    return "#"+y1+"#"+y2+"#"