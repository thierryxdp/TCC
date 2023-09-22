def hashtag(s):
    spar1 = s[0:(len(s)/2 + 1)
    spar2 = s[-1:-(len(s)/2 + 1)]
    simp2 = s[-1:-(len(s)/2 + 2)]
    if len(s) % 2 == 0:
        return "#" + spar1 + "#" + spar2
    else:
        return "#" + spar1 + "#" + simp2