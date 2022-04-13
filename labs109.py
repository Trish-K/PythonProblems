def group_and_skip(n, out, ins):
    rem_coins = []
    while n > 0:
        rem_coins.append(n%out)
        coins = n - (n%out)
        num_groups = coins // out
        n = ins*num_groups  
    return rem_coins

def is_ascending(items):
    # Flag any empty lists or lists with 1 item
    if items == [] or len(items) == 1:
        return 'True'
    # Flag any lists with duplicates
    elif len(items) != len(set(items)):
        return 'False'
    # Flag any lists that aren't ascendign
    else:
        flag = 'True'
        for count, value in enumerate(items):
            if count == 0:
                continue
            elif items[count-1] - value > 0:
                flag = 'False'
                break
        return flag

def extract_increasing(digits):
    # Create list of integers with first element = first element of digits
    ans = []
    current = int(digits[0])
    previous = -1
    digits = digits+'0'
    for d in digits[1:]:
        if current > previous:
            ans.append(current)
            previous = current
            current = int(d)   
        else:
            current = current*10 + int(d)
    return ans  

def tukeys_ninthers(items):
    if len(items) == 1:
        return items[0]
    if len(items) == 3:
        items.sort()
        return items[1]
    sublists = [items[i:i+3] for i in range(0,len(items),3)]
    med = [] 
    while len(sublists)>1:
        for sub in sublists:
            sub.sort()
            med.append(sub[1])
        sublists = [med[i:i+3] for i in range(0,len(med),3)]
        med = []
    sublists[0].sort()
    return sublists[0][1]

def safe_squares_bishops(n, bishops):
    ans = [] 
    for row in range(0,n):
        for col in range(0,n):
            for piece in bishops:
                if abs(piece[0]-row) == abs(piece[1]-col):
                    ans.append((row,col))
    return (n*n - len(set(ans)))

def brussels_choice_step(n, mink, maxk):
    #mink and maxk = num of digits you consider during a single move to *2 or /2
    #even = divide by 2 or double it 
    #odd = double by 2 only
    num = str(n)
    digit = mink
    ans = []
    
    while digit <= maxk:
        for i in range(0,len(num)):
            if i+digit>len(num):
                break
            if i == 0:
                if int(num[i:i+digit])%2 == 0:
                    ans.append(int(str(int(num[i:i+digit])//2)+num[i+digit:]))
                    ans.append(int(str(int(num[i:i+digit])*2)+num[i+digit:]))
                else:
                    ans.append(int(str(int(num[i:i+digit])*2)+num[i+digit:]))   
            elif i == len(num)-1:
                if int(num[i:i+digit])%2 == 0:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])//2)))
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)))
                else:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)))
                
            elif i != 0 and i != len(num)-1:
                if int(num[i:i+digit])%2 == 0:
                  ans.append(int(num[:i]+str(int(num[i:i+digit])//2)+num[i+digit:]))
                  ans.append(int(num[:i]+str(int(num[i:i+digit])*2)+num[i+digit:]))
                else:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)+num[i+digit:]))
                
        digit += 1
    ans.sort()
    return ans

def bulgarian_solitaire(piles, k):
    moves = 0
    test = piles[:]
    test.sort()
    if test == list(range(1,k+1)):
        return moves
    while test != list(range(1,k+1)):
        temp_len = len(test)
        test = [x-1 for x in test if x-1 > 0] 
        test += [temp_len]
        test.sort()
        moves += 1
    return moves
  
def count_carries(a, b):
    max_len = max([str(a),str(b)],key=len)
    count = 0
    carry = 0
    for i in range(0,len(str(max_len))):
        if (b%10 + a%10 + carry) >= 10:
            count += 1
        carry = (b%10 + a%10 + carry)//10
        b = b // 10
        a = a // 10
    return count

def is_left_handed(pips):
    corners = {
    (1,2,3):'LH',
    (1,2,4):'RH',
    (1,3,5):'LH',
    (1,3,2):'RH',
    (1,4,2):'LH',
    (1,4,5):'RH',
    (1,5,4):'LH',
    (1,5,3):'RH',
    (2,1,4):'LH',
    (2,1,3):'RH',
    (2,3,1):'LH',
    (2,3,6):'RH',
    (2,4,6):'LH',
    (2,4,1):'RH',
    (2,6,3):'LH',
    (2,6,4):'RH',
    (3,1,2):'LH',
    (3,1,5):'RH',
    (3,2,6):'LH',
    (3,2,1):'RH',
    (3,5,1):'LH',
    (3,5,6):'RH', 
    (3,6,5):'LH',
    (3,6,2):'RH',
    (4,1,5):'LH',
    (4,1,2):'RH',
    (4,2,1):'LH',
    (4,2,6):'RH',
    (4,5,6):'LH',
    (4,5,1):'RH',
    (4,6,2):'LH',
    (4,6,5):'RH',
    (5,1,3):'LH',
    (5,1,4):'RH',
    (5,3,6):'LH',
    (5,3,1):'RH',
    (5,4,1):'LH',
    (5,4,6):'RH',
    (5,6,4):'LH',
    (5,6,3):'RH',
    (6,2,4):'LH',
    (6,2,3):'RH',
    (6,3,2):'LH',
    (6,3,5):'RH', 
    (6,4,5):'LH',
    (6,4,2):'RH',
    (6,5,3):'LH',
    (6,5,4):'RH'}
    return corners[pips] == 'LH'

def collapse_intervals(items):
    if items == []:
        return ''
    elif len(items) == 1:
        return str(items[0])
    elif items == range(min(items),max(items)+1):
        return str(min(items))+'-'+str(max(items))
    prev = items[0]
    start = items[0]
    lst = []
    for i in items[1:]:
        if i - prev == 1 and i != items[-1]:
            prev = i
        elif i - prev ==1 and i == items[-1]:
            lst += [str(start)+'-'+str(i)]
            start = i
            prev = i
        elif i - prev != 1 and start == prev and i != items[-1]:
            lst += [str(start)]
            start = i
            prev = i
        elif i - prev != 1 and start == prev and i == items[-1]:
            lst += [str(start),str(i)]
            start = i
            prev = i
        elif i - prev != 1 and start != prev and i != items[-1]:
            lst += [str(start)+'-'+str(prev)]
            start = i
            prev = i
        elif i - prev != 1 and start != prev and i == items[-1]:
            lst += [str(start)+'-'+str(prev),str(i)]
            start = i
            prev = i
    lst = ','.join(lst)
    return lst

def collect_numbers(perm):
    ind = -1
    count = 1
    inv_perm = [0 for i in perm]  
    for i in range(0,len(perm)):
        inv_perm[perm[i]] = i
    for i in range(0,len(perm)):
        if inv_perm[i] - ind < 0:
            count += 1
        ind = inv_perm[i]
    return count

def colour_trio(colours):
    from math import factorial
    n = len(colours) - 1
    coeffs = []
    for i in range(n+1):
        coeffs.append(factorial(n)//(factorial(i)*factorial(n-i)))
    colours = list(colours)
    colour_dict = {'r':1,
                   'y':0,
                   'b':2}
    colour_dict2 = {1:'r',
                   0:'y',
                   2:'b'}
    for letter in colours:
        colours[colours.index(letter)] = colour_dict[letter]
    result = [a*b for a,b in zip(colours,coeffs)]
    if len(colours) % 2 == 0:
        final = -sum(result)%3
        return colour_dict2[final]
    final = sum(result)%3
    return colour_dict2[final]

def count_corners(points):
    h = 0
    corners = 0   
    for i, coord in enumerate(points):
        sub_points = [x for x in points if x[0] == coord[0] and x[1] > coord[1]]
        sub_points2 = [y for y in points if y[1] == coord[1] and y[0] > coord[0]]
        for j,wing in enumerate(sub_points):
            if wing[0] == coord[0] and wing[1] > coord[1]:
                h = wing[1] - coord[1]
                look4 = (coord[0]+h,coord[1])
                if look4 in sub_points2:
                    corners += 1            
    return corners

def count_consecutive_summers(n):
    start = 1
    sums = []
    ans = 0
    while start <= n:
        if sum(sums) < n:
            sums.append(start)
            start += 1
        elif sum(sums) > n:
            sums = sums[1:]
        elif sum(sums) == n:
            ans += 1
            sums = sums[1:]
    return ans+1

def count_growlers(animals):
    growl = 0
    animal_dict = {
        'cat' : 1,
        'tac' : 1,
        'dog' : -1,
        'god' : -1
    }
    vals = [animal_dict[i] for i in animals]
    for i,pet in enumerate(animals):
        if pet in ['cat','dog'] and sum(vals[:i]) < 0:
            growl += 1
        elif pet in ['tac','god'] and sum(vals[i+1:]) < 0:
            growl += 1       
    return growl

def pyramid_blocks(n, m, h):
    return sum([(n+i)*(m+i) for i in range(h)])

def count_troikas(items):
    from itertools import combinations
    pos_dict = {}
    for count,i in enumerate(items):
        if i not in pos_dict:
            pos_dict[i] = [count]
        else:
            pos_dict[i] += [count]   
    count = 0
    for key in pos_dict.keys():
        combs = list(combinations(pos_dict[key],2))
        for i in combs:
            k = i[1] + (i[1]-i[0])
            if k >= len(items):
                continue
            if items[i[0]] == items[k]:
                count += 1
    return count

def count_dominators(items):  
    if items == []:
        return 0
    if type(items) is not list:
        items = list(items)
        if items.index(max(items)) == items[-1]:
            return 1
        else:
            return len(items)
    num = 0
    count = 0
    while True:  
        if count >= len(items)-1:
            break
        elif count < len(items)-1 and items[count] > max(items[count+1:]):
            num += 1
            new_max = max(items[count+1:])
            count += items[count+1:].index(new_max) + 1
            continue
        count+=1 
    return num + 1


  

def crag_score(dice):
    # Scoring table
    dice.sort()
    scoring = {
        'crag' : 50,
        'thirteen' : 26,
        'three-of-a-kind': 25,
        'low-straight' : 20,
        'high-straight' : 20,
        'odd-straight' : 20,
        'even-straight' : 20,
    }
    if sum(dice) == 13:
        if dice != set(dice):
            num_dup = len(dice) - len(set(dice))
            if num_dup == 1:
                return scoring['crag']
        return scoring['thirteen']
    if dice != set(dice):
        num_dup = len(dice) - len(set(dice))
        if num_dup == 2:
            return scoring['three-of-a-kind']
    if dice == [1,2,3]:
        return scoring['low-straight']
    if dice == [4,5,6]:
        return scoring['high-straight']  
    if dice == [1,3,5]:
        return scoring['odd-straight']     
    if dice == [2,4,6]:
        return scoring['even-straight']
    
    score = 0
    if 6 in dice:
        score = 6*dice.count(6)
    if 5 in dice and 5*dice.count(5) > score:
        score = 5*dice.count(5)
    if 4 in dice and 4*dice.count(4) > score:
        score = 4*dice.count(4)  
    if 3 in dice and 3*dice.count(3) > score:
        score = 3*dice.count(3)    
    if 2 in dice and 2*dice.count(2) > score:
        score = 2*dice.count(2)   
    if 1 in dice and 1*dice.count(1) > score:
        score = 1*dice.count(1)    
    return score


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
        

def duplicate_digit_bonus(n):
    num_digits = len(str(n))
    last_digit = n%10
    flag = True
    k = 1
    score = 0
    for i in range(2,num_digits+1):
        if n%10**i//10**(i-1) == last_digit:
            k += 1
        elif n%10**i//10**(i-1) != last_digit and flag == True and k > 1:
            score += 2*10**(k-2)
            last_digit = n%10**i//10**(i-1)
            flag = False
            k = 1
        elif n%10**i//10**(i-1) != last_digit and flag == False and k > 1:
            score += 10**(k-2)
            last_digit = n%10**i//10**(i-1)
            flag = False
            k = 1
        elif n%10**i//10**(i-1) != last_digit and k <= 1:
            last_digit = n%10**i//10**(i-1)
            flag = False
            k = 1
            continue
    if flag == True and k > 1:
        score += 2*10**(k-2)
    elif flag == False and k > 1:
        score += 10**(k-2)
    return score
  
def knight_jump(knight, start, end):
    zip_obj = zip(start,end)
    diff = []
    for i,j in zip_obj:
        diff.append(abs(i-j))
    for i in knight:
        if i in diff:
            diff.remove(i)
        else:
            return False
    return True

def domino_cycle(tiles):
    if len(tiles) <= 1:
        return tiles == [] or tiles[0][0] == tiles[0][1] 
    elif tiles[0][0] == tiles[len(tiles)-1][1]:
        for count in range(len(tiles)-1):
            if tiles[count][1] != tiles[count+1][0]:
                return False
        return True
    return False

def only_odd_digits(n):
    if n%2 == 0:
        return False
    else:
        for digit in str(n):
            if int(digit)%2 == 0:
                return False
                break
        return True

def spread_the_coins(coins, left, right):
    ans = coins[:]
    flag = True
    ind = 0
    if len(ans) == 1 and ans[0] > left+right:
        ans = [left] + [ans[0]-(left+right)] + [right]
        ind = 1
    elif len(ans) == 1 and ans[0] < left+right:
        return (0,coins)
    elif coins == []:
        return ('',[])
    while flag:
        if ans[0] >= left+right:
            ans[0] -= left+right
            ans[1] += right
            ans = [left] + ans
            ind += 1    
        for i in range(1,len(ans)-1):
            if ans[i] >= left+right:
                ans[i-1] += left
                ans[i+1] += right
                ans[i] -= left+right         
        if ans[-1] >= left+right:
            ans[-1] -= left+right
            ans[-2] += left
            ans = ans + [right]   
        if max(ans) < left+right:
            flag = False
    for count,item in enumerate(ans):
        if item != 0:
            return (count-ind,ans[count:])
          
def give_change(amount, coins):
    rem = amount
    ans = []
    num = 0  
    for coin in coins:
        if rem >= coin:
            num = rem//coin
            rem -= coin*num
            ans += [coin]*num
        if rem == 0:
            break
    return ans

def expand_intervals(intervals):
    if intervals == '':
        return []
    int_list = intervals.split(',')
    ans = []
    for rng in int_list:
        lst = rng.split('-')
        lst = [int(x) for x in lst]
        if len(lst) == 1:
            ans += lst
        else:
            ans += list(range(lst[0],lst[1]+1))
    return ans
  
def josephus(n, k):
    ppl = list(range(1,n+1))
    d = k - 1
    if k > n and k%n != 0:
        d = k - (k//n)*n - 1
    elif k > n and k%n == 0:
        d = k - (k//n)*n - 1 + len(ppl) 
    order = []
    while len(ppl) > 1:
        if d < len(ppl):
            order.append(ppl.pop(d))
            d += k-1
        else:
            d -= len(ppl)*(d//len(ppl))
    order.append(ppl[0])
    return order  

def fractran(n, prog, giveup=1000):
    from fractions import Fraction
    all_fracs = [Fraction(i[0],i[1]) for i in prog]
    ans = [n]
    count = 0
    flag = False
    while count < giveup:
        for frac in all_fracs:
            if n*frac == int(n*frac):
                n = n*frac
                ans.append(int(n))
                flag = False
                break
            else:
                flag = True
        if flag == True:
            break
        count += 1
    return ans

def can_balance(items):
    if len(items) == 1:
        return 0  
    pos = len(items)//2
    for i in range(1,1+len(items)//2):
        l_t = sum([wt*abs(pos-j) for j,wt in enumerate(items[:pos])])
        r_t = sum([wt*(j+1) for j,wt in enumerate(items[pos+1:])])
        if l_t == r_t:
            return pos
        elif l_t > r_t:
            pos -= 1
        elif l_t < r_t:
            pos += 1     
    return -1

def squares_intersect(s1, s2):
    BL1 = [s1[0],s1[1]]
    BR1 = [s1[0]+s1[2],s1[1]]
    TL1 = [s1[0],s1[1]+s1[2]]
    TR1 = [s1[0]+s1[2],s1[1]+s1[2]]
    BL2 = [s2[0],s2[1]]
    BR2 = [s2[0]+s2[2],s2[1]]
    TL2 = [s2[0],s2[1]+s2[2]]
    TR2 = [s2[0]+s2[2],s2[1]+s2[2]]
    if BL1[0] > BR2[0] or BR1[0] < BL2[0]:
        return False
    if BL1[1] > TL2[1] or TL1[1] < BL2[1]:
        return False
    return True

def candy_share(candies):
    if max(candies) == 1:
        return 0
    rounds = 0
    curr = candies[:]
    
    while max(curr) > 1:
        for i, candy in enumerate(candies):
            if candy >= 2 and i != len(candies)-1:
                curr[i] -= 2
                curr[i-1] += 1
                curr[i+1] += 1
            elif candy >=2 and i == len(candies)-1:
                curr[i] -= 2
                curr[i-1] += 1
                curr[0] += 1
        rounds += 1
        candies = curr[:]
    return rounds   
        
def nearest_smaller(items):
    if items == []:
        return []
    if len(items) == 1:
        return items
    ans = []
    # Get answer for first item
    flag = False
    for num in items[1:]:
        if num < items[0]:
            flag = True
            ans.append(num)
            break
    if flag == False:
        ans.append(items[0])
    # Get answers for middle of items
    for i in range(1,len(items)-1):
        if items[i-1] < items[i] or items[i+1] < items[i]:
            ans.append(min([items[i-1],items[i+1]]))
        else:
            left_min = None
            right_min = None
            for j in range(1,max([len(items[:i])+1,len(items[i+1:])+1])):
                if i-j <0:
                    left_min = items[0]
                else:
                    left_min = items[i-j]
                try:
                    right_min = items[i+j]
                except:
                    right_min = right_min
                if items[i] > min([left_min,right_min]):
                    ans.append(min([left_min,right_min]))
                    break
            if items[i] <= min([left_min,right_min]):
                ans.append(items[i])
    # Get answer for last item
    flag = False
    for num in items[::-1]:
        if num < items[-1]:
            flag = True
            ans.append(num)
            break
    if flag == False:
        ans.append(items[-1])
    return ans

def recaman_item(n):
    seq = {0}
    prev = 0  
    for i in range(1,n+1):
        if prev - i > 0 and (prev-i) not in seq:
            seq.add(prev-i)
            prev = prev-i
        else:
            seq.add(prev+i)
            prev = prev+i
    return prev
  
def reverse_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    indx = []
    let = []
    ans = text[:]
    for count, letter in enumerate(text):
        if letter.lower() in vowels:
            let.append(letter)
            indx.append(count)
    let.reverse()
    for count,index in enumerate(indx):
        if text[index].isupper():
            ans = ans[:index] + let[count].upper() + ans[index+1:]
        elif text[index].islower():
            ans = ans[:index] + let[count].lower() + ans[index+1:]
    return ans

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

def safe_squares_rooks(n, rooks):
    mat = [[0 for i in range(n)] for j in range(n)]
    rows = set([y[0] for y in rooks])
    cols = set([x[1] for x in rooks])
    for y in rows:
        mat[y] = [1]*n
    for x in cols:
        for row in mat:
            row[x] = 1
    num_ones = sum([sum(i) for i in mat])
    num_zeros = n*n - num_ones
    return num_zeros
  
def seven_zero(n):
    if n%2 != 0 and n%5 !=0:
        for d in range(1,n+1):   
            num = int('7'*d)
            if num%n == 0:
                return num
    else:
        for d in range(1,n+1):
            for k in range(1,d):
                num = int('7'*k + '0'*(d-k))
                if num%n == 0:
                    return num

def oware_move(board, house):
    border = (len(board)//2)-1
    if board[house] == 0:
        return board
    count = house+1   
    while board[house] > 0:
        if count > len(board)-1:
            count = 0
            board[count] += 1
            board[house] -= 1
            count += 1
            continue
        if count == house:
            count += 1
            continue
        board[count] += 1
        count += 1
        board[house] -= 1
    
    if count == 0:
        count = len(board)-1
    else:
        count -= 1        
    if count < border:
        return board    
    for i in range(count,border,-1):
        if board[i] == 2 or board[i] == 3:
            board[i] = 0
        else:
            break            
    return board

def words_with_letters(words, letters):
    ans = []
    for word in words: 
        if letters[0] in word:
            ind = word.index(letters[0])
            flag = True
            for i in letters[1:]:
                if i in word[ind+1:] and ind < (word[ind+1:].index(i) + ind + 1):
                    ind = ind + word[ind+1:].index(i) + 1
                else:
                    flag = False
                    break
            if flag == True:
                ans.append(word)
    return ans   
  
def sum_of_two_squares(n):
    i = 1
    j = int(n**(1/2))
    while i <= j:
        if (j**2 + i**2) == n:
            return (j,i)
        elif (j**2 + i**2) < n:
            i += 1
        elif (j**2 + i**2) > n:
            j -= 1          
    return None

def taxi_zum_zum(moves):
    rot = 90
    pos = [0,0] 
    move_dict = {
        'L':90,
        'R':-90,
        'F':1}
    for move in moves:
        if move in ['R','L']:
            rot += move_dict[move]   
            if rot > 360:
                rot -= 360
            elif rot < 0: 
                rot += 360       
        else:    
            if rot == 90 and move == 'F':
                pos[1] += move_dict[move]
            elif rot == 270 and move == 'F':
                pos[1] -= move_dict[move]
            elif rot == 0 or rot == 360 and move == 'F':
                pos[0] += move_dict[move]
            elif rot == 180 and move == 'F':
                pos[0] -= move_dict[move]
    return tuple(pos)

def first_preceded_by_smaller(items, k=1):
    if isinstance(items[0],int) or isinstance(items[0],float): 
        for count,i in enumerate(items[1:]):
            smaller_items = [x for x in items[:count+1] if x < i]
            if len(smaller_items) >= k:
                return i
        return None
    elif isinstance(items[0],str):
        for count,i in enumerate(items[1:]):
            smaller_items = [x for x in items[:count+1] if len(x) < len(i)]
            if len(smaller_items) >= k:
                return i
        return None 

def remove_after_kth(items, k=1):
    my_dict = {}
    ans = []
    for i in items:
        if i not in my_dict:
            my_dict[i] = 1
        elif i in my_dict:
            my_dict[i] += 1
        if my_dict[i] <= k:
            ans.append(i)        
    return ans

def winning_card(cards, trump=None):
    card_dict = {
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'jack':11,
        'queen':12,
        'king':13,
        'ace':14
    }   
    trump_plays = [play for play in cards if play[1] == trump]   
    if trump == None or trump_plays == []:
        winner = cards[0]
        for play in cards[1:]:
            if play[1] == winner[1] and card_dict[play[0]] > card_dict[winner[0]]:
                winner = play
        return winner
    if trump != None:
        winner = trump_plays[0]
        for play in trump_plays:
            if card_dict[play[0]] > card_dict[winner[0]]:
                winner = play
        return winner
        
def three_summers(items, goal):
    if goal <= max(items):
        new_goal = [count for count, x in enumerate(items) if x <= goal]
        goal_ind = max(new_goal)        
        for i in range(0,len(items[:goal_ind+1])-1):
            start = items[i]
            for k in range(len(items[:goal_ind+1])-1,i,-1):   
                end = items[k]
                if (goal-(start+end)) in items[i+1:k]:
                    return True
        return False       
    for i in range(len(items)-1,-1,-1):
        start = items[i]
        for k in range(i-1,-1,-1):
            end = items[k]
            if (goal - (start + end)) in items[:k]:
                return True
    return False  

def pancake_scramble(text):
    new_text = text
    for i in range(len(text)):
        if i == 0:
            continue            
        new_text = new_text[i-1::-1] + new_text[i:]
    return new_text[::-1]
  
def count_and_say(digits):
    if digits == '':
        return ''
    elif len(digits) == 1:
        return '1' + digits    
    start = digits[0]
    count = 1
    ans = ''
    for i in digits[1:]:
        if i == start:
            count += 1
        elif i != start:
            ans = ans + str(count) + start
            start = i
            count = 1
    return ans + str(count) + digits[-1]
  
def words_with_given_shape(words, shape):
    ans = []
    nums = []
    for word in words:
        if len(word)-1 != len(shape):
            continue            
        nums = [ord(i) for i in word]
        flag = True        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 0 and shape[i] != 0:
                flag = False
                break
            elif nums[i+1]-nums[i] > 0 and shape[i] < 0:
                flag = False
                break
            elif nums[i+1]-nums[i] < 0 and shape[i] > 0:
                flag = False
                break
            else:
                flag = True                
        if flag == True:
            ans.append(word)                
    return ans

def calkin_wilf(n):
    from fractions import Fraction
    from collections import deque    
    count = 1    
    prev = deque([Fraction(1,1)])
    left = None
    right = None
    end_point = n    
    while count < end_point:
        consider = prev.popleft()
        left = Fraction(consider.numerator, (consider.numerator + consider.denominator))
        right = Fraction((consider.numerator + consider.denominator), consider.denominator)
        prev.append(left)
        prev.append(right)        
        count += 1     
    return prev.popleft()

def conjugate_regular(verb, subject, tense):
    ar_dict = {
        'yo' : 'o',
        'tú' : 'as',
        'él' : 'a',
        'ella' : 'a', 
        'usted' : 'a',
        'nosotros' : 'amos',
        'nosotras' : 'amos',
        'vosotros' : 'áis',
        'vosotras' : 'áis',
        'ellos' : 'an',
        'ellas' : 'an',
        'ustedes' : 'an'
    }    
    er_dict = {
        'yo' : 'o',
        'tú' : 'es',
        'él' : 'e',
        'ella' : 'e', 
        'usted' : 'e',
        'nosotros' : 'emos',
        'nosotras' : 'emos',
        'vosotros' : 'éis',
        'vosotras' : 'éis',
        'ellos' : 'en',
        'ellas' : 'en',
        'ustedes' : 'en'
    }    
    ir_dict = {
        'yo' : 'o',
        'tú' : 'es',
        'él' : 'e',
        'ella' : 'e', 
        'usted' : 'e',
        'nosotros' : 'imos',
        'nosotras' : 'imos',
        'vosotros' : 'ís',
        'vosotras' : 'ís',
        'ellos' : 'en',
        'ellas' : 'en',
        'ustedes' : 'en'
    }    
    ar_pret = {
        'yo' : 'é',
        'tú' : 'aste',
        'él' : 'ó',
        'ella' : 'ó', 
        'usted' : 'ó',
        'nosotros' : 'amos',
        'nosotras' : 'amos',
        'vosotros' : 'asteis',
        'vosotras' : 'asteis',
        'ellos' : 'aron',
        'ellas' : 'aron',
        'ustedes' : 'aron'
    }
    er_ir_pret = {
        'yo' : 'í',
        'tú' : 'iste',
        'él' : 'ió',
        'ella' : 'ió', 
        'usted' : 'ió',
        'nosotros' : 'imos',
        'nosotras' : 'imos',
        'vosotros' : 'isteis',
        'vosotras' : 'isteis',
        'ellos' : 'ieron',
        'ellas' : 'ieron',
        'ustedes' : 'ieron'
    }    
    ar_imp = {
        'yo' : 'aba',
        'tú' : 'abas',
        'él' : 'aba',
        'ella' : 'aba', 
        'usted' : 'aba',
        'nosotros' : 'ábamos',
        'nosotras' : 'ábamos',
        'vosotros' : 'abais',
        'vosotras' : 'abais',
        'ellos' : 'aban',
        'ellas' : 'aban',
        'ustedes' : 'aban'
    }    
    er_ir_imp = {
        'yo' : 'ía',
        'tú' : 'ías',
        'él' : 'ía',
        'ella' : 'ía', 
        'usted' : 'ía',
        'nosotros' : 'íamos',
        'nosotras' : 'íamos',
        'vosotros' : 'íais',
        'vosotras' : 'íais',
        'ellos' : 'ían',
        'ellas' : 'ían',
        'ustedes' : 'ían'
    }    
    fut_dict = {
        'yo' : 'é',
        'tú' : 'ás',
        'él' : 'á',
        'ella' : 'á', 
        'usted' : 'á',
        'nosotros' : 'emos',
        'nosotras' : 'emos',
        'vosotros' : 'éis',
        'vosotras' : 'éis',
        'ellos' : 'án',
        'ellas' : 'án',
        'ustedes' : 'án'
    }   
    ending = verb[-2:]
    if tense == 'presente':
        if ending == 'ar':
            return verb[:-2] + ar_dict[subject]
        elif ending == 'er':
            return verb[:-2] + er_dict[subject]
        elif ending == 'ir':
            return verb[:-2] + ir_dict[subject]     
    elif tense == 'pretérito':
        if ending == 'ar':
            return verb[:-2] + ar_pret[subject]
        elif ending == 'er' or ending == 'ir':
            return verb[:-2] + er_ir_pret[subject]    
    elif tense == 'imperfecto':
        if ending == 'ar':
            return verb[:-2] + ar_imp[subject]
        elif ending == 'er' or ending == 'ir':
            return verb[:-2] + er_ir_imp[subject]        
    elif tense == 'futuro':
        return verb + fut_dict[subject]    
    return ''


def postfix_evaluate(items):
    lst = []
    ans = 0
    for i in items:
        if isinstance(i,int):
            lst.append(i)
        elif not isinstance(i,int):
            if i == '/' and lst[-1] == 0:
                ans = 0
                lst = lst[:-2] + [ans]
            elif i == '/':
                i = '//'
                ans = eval(str(lst[-2])+ i + str(lst[-1]))
                lst = lst[:-2] + [ans]    
            else:
                ans = eval(str(lst[-2])+ i + str(lst[-1]))
                lst = lst[:-2] + [ans]
    return lst[0]

def ztalloc(shape):
    if 'uu' in shape:
        return None
    start = 1
    step = [start]   
    for move in shape[::-1]:
        if move == 'd':
            start = start * 2
            step.append(start)
        elif move == 'u' and start%2 == 0:
            if (start - 1)/3 == (start - 1)//3:
                start = (start - 1)//3
                step.append(start)
            else:
                return None
        elif move == 'u' and start%2 != 0:
            return None
    return step[-1]

def brangelina(first, second):
    vowels = 'aeiou'
    count_vowels = []
    prev = False
    count = 0
    for i,letter in enumerate(first):
        if letter in vowels and prev == False:
            count_vowels.append(i)
            prev = True
            count += 1
        elif letter in vowels and prev == True:
            continue
        else:
            prev = False
    beg = ''
    if len(count_vowels) == 1:
        beg = first[:count_vowels[0]]
        if second[0] in vowels:
            return beg + second
        else:
            for i,letter in enumerate(second):
                if letter in vowels:
                    return beg + second[i:]
    elif len(count_vowels) > 1:
        beg = first[:count_vowels[-2]]
        if second[0] in vowels:
            return beg + second
        else:
            for i,letter in enumerate(second):
                if letter in vowels:
                    return beg + second[i:]
                
def count_divisibles_in_range(start, end, n):
    count = end//n - start//n
    if start%n == 0:
        return count + 1
    return end//n - start//n

def bridge_hand_shape(hand):
    hand_dict = {
        'spades' : 0,
        'hearts' : 0,
        'diamonds' : 0,
        'clubs' : 0
    }
    for card in hand:
        hand_dict[card[1]] += 1    
    return [hand_dict['spades'], hand_dict['hearts'], hand_dict['diamonds'], hand_dict['clubs']]

def milton_work_point_count(hand, trump='notrump'):
    card_dict = {
        'spades' : 0,
        'hearts' : 0,
        'diamonds' : 0,
        'clubs' : 0} 
    num_dict = {
        'one' : [],
        'two' : [],
        'three' : [],
        'four' : [],
        'five' : [],
        'six' : [],
        'seven' : [],
        'eight' : [],
        'nine' : [],
        'ten' : [],
        'jack' : [],
        'queen' : [],
        'king' : [],
        'ace' : []}
    points = 0
    
    for card in hand:
        card_dict[card[1]] += 1
        if num_dict[card[0]] == []:
            num_dict[card[0]] = [card[1]]
        else:
            num_dict[card[0]] = num_dict[card[0]] + [card[1]]
            
        if card[0] == 'ace':
            points += 4
        elif card[0] == 'king':
            points += 3
        elif card[0] == 'queen':
            points += 2     
        elif card[0] == 'jack':
            points += 1
    card_counts = [card_dict['spades'], card_dict['hearts'], card_dict['diamonds'], card_dict['clubs']]
    card_counts.sort()
    if card_counts == [3,3,3,4]:
        points -= 1        
    for key in card_dict.keys():
        if card_dict[key] == 5:
            points += 1
        elif card_dict[key] == 6:
            points += 2
        elif card_dict[key] >= 7:
            points += 3       
    if trump != 'notrump':
        for key in card_dict.keys():
            if card_dict[key] == 0 and key != trump:
                points += 5
            elif card_dict[key] == 1 and key != trump:
                points += 3    
    return points