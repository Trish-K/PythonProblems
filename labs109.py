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


