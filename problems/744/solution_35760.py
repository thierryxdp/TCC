def hashtag (string):
hashtag = '#'+string+'#'
meio = len(string)//2
hashtag = string[:meio] + '#' + string[meio:]

return hashtag