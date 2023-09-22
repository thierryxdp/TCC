string = input(''Digite a string: '')
string = '#'+string+'#'
meio = len(string)//2
string = string[:meio] + '#' + string[meio:]
return string