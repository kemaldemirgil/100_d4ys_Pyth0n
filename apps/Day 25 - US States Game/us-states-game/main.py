import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses_states = []

def hide_turtle():
  t = turtle.Turtle()
  t.hideturtle()
  t.penup()
  return t

def write_state(data):
  t = hide_turtle()
  t.goto(int(data.x), int(data.y))
  t.write(answer_state)

def get_missing_states():
  missing_states = []
  for state in all_states:
    if state not in guesses_states:
      missing_states.append(state)
  return missing_states


def exit_game(answer_state):
  if answer_state == "Exit":
    new_data = pandas.DataFrame(get_missing_states())
    new_data.to_csv("states_to_learn.csv")
    return True
  return False

def get_state(answer_state):
  if answer_state in all_states:
    guesses_states.append(answer_state)
    state_data = data[data.state == answer_state]
    write_state(state_data)

def get_answer():
  answer = screen.textinput(title=f"{len(guesses_states)}/50 States Correct", prompt="What's another state's name?").title()
  return answer


while len(guesses_states) < 50:
  answer_state = get_answer()
  if exit_game(answer_state):
    break
  get_state(answer_state)