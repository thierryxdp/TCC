def walrus():
  roll_count = 1
  while (rolls := roll())[0] != rolls[1]:
    roll_count += 1
  return (roll_count, rolls)