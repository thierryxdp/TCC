def hashtag(marte):
    marte = "#" + marte[:len(marte)//2] + "#" + marte[len(marte)//2:] + "#"
    return marte