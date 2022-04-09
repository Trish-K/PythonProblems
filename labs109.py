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
#         print(f'current = {current}')
#         print(f'previous = {previous}')
#         print(f'd = {d}')
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
#             print(f'sub = {sub}')
            sub.sort()
            med.append(sub[1])
#             print(f'median = {med}')
        sublists = [med[i:i+3] for i in range(0,len(med),3)]
        med = []
#         print(f'new sublists = {sublists}')

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
#         print(f'digit = {digit}')
        for i in range(0,len(num)):
            if i+digit>len(num):
#                 print('too long')
                break
            if i == 0:
#                 print(f'adjust {num[i:i+digit]} + {num[i+digit:]}')
                if int(num[i:i+digit])%2 == 0:
                    ans.append(int(str(int(num[i:i+digit])//2)+num[i+digit:]))
                    ans.append(int(str(int(num[i:i+digit])*2)+num[i+digit:]))
                else:
                    ans.append(int(str(int(num[i:i+digit])*2)+num[i+digit:]))
                
            elif i == len(num)-1:
#                 print(f'{num[:i]} + adjust {num[i:i+digit]}')
                if int(num[i:i+digit])%2 == 0:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])//2)))
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)))
                else:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)))
                
            elif i != 0 and i != len(num)-1:
#                 print(f'{num[:i]} + adjust {num[i:i+digit]} + {num[i+digit:]}')
                if int(num[i:i+digit])%2 == 0:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])//2)+num[i+digit:]))
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)+num[i+digit:]))
                else:
                    ans.append(int(num[:i]+str(int(num[i:i+digit])*2)+num[i+digit:]))
                
#         print(f'at the end of this round ans = {sorted(ans)}')
        digit += 1
    ans.sort()
    return ans

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
#         print(f'i = {i}, prev = {prev}, start = {start}')
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
##    ind = 0
    ind = -1
    count = 1
##    inv_perm = []
    inv_perm = [0 for i in perm]  
    # Check for ranges that go up by 1        
    # if list(range(min(perm),max(perm)+1)) == perm:
    #     return 1

    # Check for ranges that go down by 1
    # if list(range(max(perm),min(perm)-1,-1)) == perm:
    #     return len(perm)
   
    # Continue finding the inverse for all other cases
    # for i in range(0,len(perm)):
    #     inv_perm.append(perm.index(i))
    for i in range(0,len(perm)):
        inv_perm[perm[i]] = i
       
    for i in range(0,len(perm)):
        if inv_perm[i] - ind < 0:
#             print(f'index = {inv_perm[i]} minus position {ind}')
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
#                 print(look4)
                if look4 in sub_points2:
                    corners += 1

                
    return corners

def count_consecutive_summers(n):
    start = 1
    sums = []
    ans = 0
    while start <= n:
#         print(f'sums contains {sums}')
#         print(f'the sum of sums is {sum(sums)}')
        
        if sum(sums) < n:
#             print(f'smaller than n!')
            sums.append(start)
            start += 1
        elif sum(sums) > n:
#             print(f'greater than n!')
            sums = sums[1:]
        elif sum(sums) == n:
#             print(f'equals n!')
            ans += 1
            sums = sums[1:]
#         print(f'-------------------------')
        
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
    
#     print(pos_dict)
    
    count = 0
    for key in pos_dict.keys():
        combs = list(combinations(pos_dict[key],2))
#         print(combs)
        for i in combs:
            k = i[1] + (i[1]-i[0])
#             print(f'i = {i[0]}, j = {i[1]}, and k = {k}')
            if k >= len(items):
                continue
            if items[i[0]] == items[k]:
#                 print(f'therefore i = {items[i[0]]}, j = {items[i[1]]}, and k = {items[k]}')
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
#             print('new max is {}'.format(new_max))
#             print('count is {}'.format(count))
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
#         print(f'digit of interest = {n%10**i//10**(i-1)}')
        if n%10**i//10**(i-1) == last_digit:
            k += 1
#             print(f'True! k now equals = {k}')
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
    
#     print(f'k = {k} and d = {d}')
    
    order = []
    
    while len(ppl) > 1:
#         print(f'd = {d} and ppl = {ppl} and order = {order}')
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
#             print(f'try n*frac: {n}*{frac} = {n*frac}')
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
#         print(f'pos = {pos}')
        l_t = sum([wt*abs(pos-j) for j,wt in enumerate(items[:pos])])
        r_t = sum([wt*(j+1) for j,wt in enumerate(items[pos+1:])])
#         print(f'left_torque = {l_t} and right_torque = {r_t}')
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
        
#         print(f'before round curr = {curr} and candies = {candies}')
        for i, candy in enumerate(candies):
#             print(f'i = {i} and candy = {candy}')
            if candy >= 2 and i != len(candies)-1:
                curr[i] -= 2
                curr[i-1] += 1
                curr[i+1] += 1
            elif candy >=2 and i == len(candies)-1:
                curr[i] -= 2
                curr[i-1] += 1
                curr[0] += 1
#         print(f'after round curr = {curr} and candies = {candies}')
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
#         print(f'look for solution for item = {items[i]}')
        if items[i-1] < items[i] or items[i+1] < items[i]:
            ans.append(min([items[i-1],items[i+1]]))
        else:
            left_min = None
            right_min = None
            for j in range(1,max([len(items[:i])+1,len(items[i+1:])+1])):
#                 print(f'i = {i} and j = {j} therefore i+j = {i+j}')
                if i-j <0:
                    left_min = items[0]
                else:
                    left_min = items[i-j]
                try:
                    right_min = items[i+j]
                except:
                    right_min = right_min
#                 print(f'left_min = {left_min} and right_min = {right_min}')
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
#         print(f'prev = {prev} and i = {i}')
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
#     print(let)
#     print(indx)
    for count,index in enumerate(indx):
        if text[index].isupper():
            ans = ans[:index] + let[count].upper() + ans[index+1:]
        elif text[index].islower():
            ans = ans[:index] + let[count].lower() + ans[index+1:]
#         print(ans)
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
#             print(f'd = {d} and num = {num}')
            if num%n == 0:
                return num

#     for d in range(1,len(str(n))+3):
    else:
        for d in range(1,n+1):
            for k in range(1,d):
    #             print(f'd = {d} and k = {k}')
                num = int('7'*k + '0'*(d-k))
    #             yield num
    #             print(num)
                if num%n == 0:
                    return num



def oware_move(board, house):
    border = (len(board)//2)-1
    if board[house] == 0:
        return board
    
    count = house+1
    
    while board[house] > 0:
        # print(f'count = {count}')
        if count > len(board)-1:
            count = 0
            board[count] += 1
            board[house] -= 1
            count += 1
            # print(f'board = {board}')
            continue
        if count == house:
            count += 1
            continue
        board[count] += 1
        count += 1
        board[house] -= 1
        # print(f'board = {board}')
    
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
    for word in words: #[41174:41175]: #[41176:41178]: #[37893:37900]:  
#             print(word)
        if letters[0] in word:
            ind = word.index(letters[0])
            flag = True
            for i in letters[1:]:
#                     print(f'check for letter {i} at index {ind} and on')
#                     print(word[ind:])
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
    pos = [0,0] #x,y
    move_dict = {
        'L':90,
        'R':-90,
        'F':1}
    for move in moves:
        if move in ['R','L']:
#             print(f'move = {move} and rotation previously = {rot}')
            rot += move_dict[move]   
            if rot > 360:
                rot -= 360
            elif rot < 0: 
                rot += 360
#             print(f'rotation after = {rot}')
            
        else:    
#             print(f'Move = {move}')
            if rot == 90 and move == 'F':
                pos[1] += move_dict[move]
            elif rot == 270 and move == 'F':
                pos[1] -= move_dict[move]
            elif rot == 0 or rot == 360 and move == 'F':
                pos[0] += move_dict[move]
            elif rot == 180 and move == 'F':
                pos[0] -= move_dict[move]
#         print(f'Position after = {pos}')
#         print(f'----------------------------------------')
        
    return tuple(pos)


def first_preceded_by_smaller(items, k=1):
    if isinstance(items[0],int) or isinstance(items[0],float): 
        for count,i in enumerate(items[1:]):
            smaller_items = [x for x in items[:count+1] if x < i]
#             print(f'i is {i}')
#             print(f'smaller items up till i is {smaller_items}')
            if len(smaller_items) >= k:
                return i
        return None

    elif isinstance(items[0],str):
        for count,i in enumerate(items[1:]):
            smaller_items = [x for x in items[:count+1] if len(x) < len(i)]
#             print(f'i is {i}')
#             print(f'smaller items up till i is {smaller_items}')
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
#                 print(f'i = {i}, k = {k}, start = {start}, end = {end}')
                if (goal-(start+end)) in items[i+1:k]:
                    return True
        return False
        
    for i in range(len(items)-1,-1,-1):
        start = items[i]
        for k in range(i-1,-1,-1):
            end = items[k]
#             print(f'i = {i}, k = {k}, start = {start}, end = {end}, rem = {items[:k]}')
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
#         print(f'we are looking for {start}')
#         print(f'the current number is {i}')
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
