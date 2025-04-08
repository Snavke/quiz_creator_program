# dictionary to store inputs
dict_questions = {}
dict_choices = {}
dict_answer = {}

# User provides questions
while True:
    question_input = input("Enter Question: ")
    choices_input = input("Enter 4 Possible Choices: ")
    answer_input = input("Enter Answer (The Letter): ")

    dict_questions = {"Question": question_input}
    dict_choices = {"Choices": choices_input}
    dict_answer ={"Answer": answer_input}

    exit_prompt = input("Continue adding question? (yes/no): ").lower

    if exit_prompt != "yes":
        break

print (dict_questions, dict_choices, dict_answer)
# User provides possible choices

# User provides correct answer from possible choices



print ()
# Confirm questions, choice, and answers, give option to redo

# Continue asking until user chooses to terminate program

# Add functionality to choose question to delete, or to edit (will overwrite)

# Store collected data per user "session" to text file