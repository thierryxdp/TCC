def hashtag(s):'''retorna uma string com '#' no meio
    str-->str'''
    numeros= len(s)//2
    return "#"+s[:numeros]+"#"+s[numeros:]"#"