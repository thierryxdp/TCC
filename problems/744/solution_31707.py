def hashtag(word):
    word1=(str(word[:len(word)//2]))
    word2=(str(word[len(word)//2:]))
    return '#'+word1+'#'+word2+'#'