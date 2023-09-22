def hashtag(x):
    """Calcula e retorna a expressao da
string "x" mais o caracter"#" no ínico,
meio e fim da string "x"; str --> str"""
    y="#"+(x[0:(floor((len(x))/2))])+"#"+
(x[(floor((len(x))/2)):])+"#"
    return y