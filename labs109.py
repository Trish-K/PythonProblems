# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > 6:
#         adjust = "+"
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust

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

# 16 seconds
# def is_ascending(items):
#     flag = 'True'
#     if items == [] or len(items) == 1:
#         return 'True'
#     else:
#         for count, value in enumerate(items):
#             if count == 0:
#                 continue
#             elif value > items[count-1]:
#                 continue
#             elif value <= items[count-1]:
#                 flag = 'False'
#                 break
#     return flag

# 15.4 seconds
# def is_ascending(items):
#     # Flag any empty lists or lists with 1 item
#     if items == [] or len(items) == 1:
#         return 'True'
#     # Flag any lists with duplicates
#     elif len(items) != len(set(items)):
#         return 'False'
#     # Flag any lists that aren't ascendign
#     else:
#         flag = 'True'
#         for count, value in enumerate(items):
#             if count == 0:
#                 continue
#             elif items[count-1] - value > 0:
#                 flag = 'False'
#                 break
#         return flag

# 15.2 seconds
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
        for count in range(len(items)-1):
            if items[count+1] - items[count] < 0:
                flag = 'False'
                break
        return flag

def riffle(items, out=True):
    if items == []:
        return []
    elif out == True:
        rifl = []
        for count in range(len(items)//2):
            rifl.append(items[count])
            rifl.append(items[count-len(items)//2])
        return rifl
    elif out == False:
        rifl = []
        for count in range(len(items)//2):
            rifl.append(items[count-len(items)//2])
            rifl.append(items[count])
        return rifl
