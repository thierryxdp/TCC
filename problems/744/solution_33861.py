def hashtag(s):
    "Coloca # no início, meio e fim da palavra"
    "str -> str"
    return "#"+s[ :(len(s)/2)]+"#"+s[(len(s)/2): ]+"#"