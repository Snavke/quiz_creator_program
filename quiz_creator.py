# list to store inputs
list_questions = []
list_choices = []
list_answer = []

# User provides questions

question_input = input("Enter Question: ")
list_questions.append(question_input) 

# User provides possible choices
choices_input = input("Enter 4 Possible Choices: ")
list_choices.append(choices_input)

# User provides correct answer from possible choices
answer_input = input("Enter Answer (The Letter): ")
list_answer.append(answer_input)


print (list_questions, list_choices, list_answer)
# Confirm questions, choice, and answers, give option to redo

# Continue asking until user chooses to terminate program

# Add functionality to choose question to delete, or to edit (will overwrite)

# Store collected data per user "session" to text file