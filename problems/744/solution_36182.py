def hashtag(x):
    """Calcula e retorna a expressao da
string "x" mais o caracter"#" no ínico,
meio e fim da string "x"; str --> str"""
    y1="#"+(x[0:(floor((len(x))/2))])+"#"
  	y2=(x[(floor((len(x))/2)):])+"#"
    return y1+y2