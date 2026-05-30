# =========================
# Question 6 — Turtle Archery Game
# =========================

"""
A student is creating a turtle archery game.

The game stores all player information
inside a list containing one dictionary.

Tasks:
1. Move each turtle object using positions
   from "position_list"

2. Write the player name using "nameboard"

3. Increase the player's score by 10

4. Write the updated score using "scoreboard"
"""

import turtle

screen = turtle.Screen()

player_list = [
    {
        "name": "Alicia",
        "score": 0,
        "arrow": turtle.Turtle(),
        "target": turtle.Turtle(),
        "nameboard": turtle.Turtle(),
        "scoreboard": turtle.Turtle(),
        "position_list": [
            (100, 50),
            (-150, 120),
            (0, -100),
            (200, 80)
        ]
    }
]

player = player_list[0]
player_list[0]["arrow"].penup()
player_list[0]["arrow"].goto(player_list[0]["position_list"][0])
player_list[0]["target"].penup()
player_list[0]["target"].goto(player_list[0]["position_list"][1])
player_list[0]["scoreboard"].penup()
player_list[0]["scoreboard"].goto(player_list[0]["position_list"][0])
player_list[0]["scoreboard"].write("10")
player_list[0]["scoreboard"].hideturtle()
player_list[0]["nameboard"].penup()
player_list[0]["nameboard"].hideturtle()
player_list[0]["nameboard"].goto(player_list[0]["position_list"][2])
player_list[0]["nameboard"].write("alicia")

# move arrow turtle to first position

# move target turtle to second position

# move nameboard turtle to third position

# move scoreboard turtle to fourth position

# write player name using nameboard turtle

# increase score by 10

# write score using scoreboard turtle
while True:
    screen.update()

print(player["score"])
