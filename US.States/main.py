import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guess_list = []
score =0
while len(guess_list) < 50:
    answer = screen.textinput(f"{score}/50 states correct!", "Enter the state's name").title()

    if answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_list:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("statesToLearn.csv")
        break
    if answer in all_states:
        score += 1
        guess_list.append(answer)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer)
















screen.exitonclick()


