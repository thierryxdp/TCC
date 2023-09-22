def hashtag(s):
    "recebe como entrada uma sring e acrecenta o simbolo # no inicio da string, no meio e no final dela"
    "string->string"
    s= "#"+s+"#"
    meio= len(s)//2
    s= s[:meio]+"#"+s[meio:]
    return(s)