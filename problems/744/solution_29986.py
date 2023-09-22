def  hashtag (s):
    #pre = s [: len (s) // 2]
    #pos = s [len (s) // 2:]
    # s = "#" + pre + "#" + pos + "#"
    s  =  "#"  +  s [: len (s) // 2 ] +  "#"  +  s [ len ( s ) // 2 :] +  "#"
    return  s