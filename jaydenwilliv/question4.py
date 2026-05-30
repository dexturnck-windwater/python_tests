
# =========================
# Question 4 — Function Debugging
# =========================

"""
A student is making a score calculator program,
but the code has an error.

Tasks:
1. Find the error
2. Fix the code
3. Explain why the error happens        
error happens becaude  "bonus" have double quote it suppos to be a interger                                    Q   Q   
"""

name = "Alicia"
score1 = 80
score2 = 90
bonus = 5

def calculate_total(a, b, extra):
    total = a + b + extra
    return total

def show_result(student, total_score):
    print("Student:", student)
    print("Total Score:", total_score)

print("=== Student Result System ===")

total = calculate_total(score1, score2, bonus)

if total >= 170:
    print("Excellent")
else:
    print("Good")

show_result(name, total)
