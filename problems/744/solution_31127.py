"função que retorna uma concataneção de strings dado uma inicial, que resulta em uma string com um hastag no início, no meio e no fim dela"
"str->str"

def hashtag(x):
    x=x[0:len(x)//2]+"#"+x[len(x)//2:]
    return "#"+x+"#"