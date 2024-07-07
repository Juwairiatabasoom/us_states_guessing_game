import turtle
import pandas as pd

screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's the another state?").title()
    if answer=="Exit":
        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)
        new_data=pd.DataFrame(remaining_states)
        new_data.to_csv("remaining_states.csv")
        break
    if answer in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer) #or t.write(state_data.state.item() it prints only the first word
        all_states.remove(answer) #to not allow the answer to br guessed twice
        guessed_states.append(answer)






