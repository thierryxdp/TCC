# str-> str
def meio(x):
    return (len(x))/2
def hashtag(x):
    return "#"+x[0:(meio(x))]+"#"+x[meio(x):len(x)]+"#"