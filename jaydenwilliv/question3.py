# =========================
# Question 3 — Shop Status Switch
# =========================

"""
A shop owner wants a simple program to change the shop
status every morning and night.

- If the shop is currently "open",
  change it to "close"

- If the shop is currently "close",
  change it to "open"

Theory Question:
Should this program use:
- two if statements
- or if with elif

Explain your answer.
more affective
"""

shop = input("Enter shop status (open/close): ")
if shop=="open":
    shop="close"
elif shop=="close":
    shop="open"
print("New shop status:", shop)