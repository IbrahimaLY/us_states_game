import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    if answer_state == "Exit":
        # Méthode 1 : Compréhension de liste
        states_to_learn = [state for state in all_states if state not in guessed_states]

        # Convertir en ensembles et calculer la différence
        states_to_learn2 = list(set(all_states) - set(guessed_states))

        df = pd.DataFrame(states_to_learn2)
        df.to_csv("states_to_learn.csv", index=False, header=False)
        break

    if answer_state in all_states:
        timi = Turtle()
        timi.hideturtle()
        timi.penup()
        state_data = data[data.state == answer_state]
        timi.goto(state_data.x.item(), state_data.y.item())
        timi.write(answer_state)
        guessed_states.append(answer_state)



# Auteur : Ibrahima Oumar LY
# Github name: IbrahimaLY
# Date de cr�ation : {date}
# Description : Ce fichier contient les fonctions pour le jeu U.S. States.

