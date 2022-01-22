def ryerson_letter_grade(pct):
  if 90 <= pct <= 100 or 100 <= pct <= 150:
    return 'A+'
  elif 85 <= pct <= 89:
    return 'A'
  elif 80 <= pct <= 84:
    return 'A-'
  elif 77 <= pct <= 79:
    return 'B+'
  elif 73 <= pct <= 76:
    return 'B'
  elif 70 <= pct <= 72:
    return 'B-'
  elif 67 <= pct <= 69:
    return 'C+'
  elif 63 <= pct <= 66:
    return 'C'
  elif 60 <= pct <= 62:
    return 'C-'
  elif 57 <= pct <= 59:
    return 'D+'
  elif 53 <= pct <= 56:
    return 'D'
  elif 50 <= pct <= 52:
    return 'D-'
  elif 0 <= pct <= 49:
    return 'F'


# 15.2 seconds
def is_ascending(items):
  return sorted(items) == items and len(set(items)) == len(items)

def riffle(items, out=True):
  if out:
    rifl = []
    for count in range(len(items)//2):
      rifl.append(items[count])
      rifl.append(items[count-len(items)//2])
    return rifl
  else:
    rifl = []
    for count in range(len(items)//2):
      rifl.append(items[count-len(items)//2])
      rifl.append(items[count])
    return rifl

def only_odd_digits(n):
  if n%2 == 0:
    return False
  else:
    for digit in str(n):
      if int(digit)%2 == 0:
        return False
        break
    return True

def is_cyclops(n):
  if n == 0:
    return True
  elif len(str(n))%2 == 0:
    return False
  elif str(n).count('0') > 1:
    return False
  elif str(n)[(len(str(n))-1)//2] == '0':
    return True
  return False

def domino_cycle(tiles):
  if len(tiles) <= 1:
    return tiles == [] or tiles[0][0] == tiles[0][1] 
  elif tiles[0][0] == tiles[len(tiles)-1][1]:
    for count in range(len(tiles)-1):
      if tiles[count][1] != tiles[count+1][0]:
        return False
    return True
  return False