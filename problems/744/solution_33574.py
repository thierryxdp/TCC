def hashtag(s):
     i=len(s)
     f=i//2
     
     return "#"+ s[:f+1]+"#"+ s[f+1:]+"#"