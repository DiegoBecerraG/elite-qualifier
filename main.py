def init_chat():
  quit_character = 'q'

  name = input("You know, you haven't told me your name? What's your name?\n")
  print("That's a nice name")
  user_input = input("Well then " + name + ", how do you do?\n")
  while user_input != quit_character:
    user_input = input("Is that so?\n")
    user_input = input("Hey " + name + ", you know what always gets me in a good mood? It's talking about food. What's your favorite food?\n")
    user_input = input("Oh yeah, I've heard of that before. Since you like it it must be good huh?\n")
    print("That's great to hear!")
    user_input = input("Well, that was a fun conversation. Do you wish this past conversation?")
  print("It was great talking with you. Have a good day!")

if __name__ == "__main__":
  init_chat()