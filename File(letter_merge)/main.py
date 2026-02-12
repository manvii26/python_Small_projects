"""
main.py

This program generates personalized invitation letters.

Steps:
Reads all invited names from a text file.
Reads a template letter containing a placeholder [name].
Replaces the placeholder with each person's name.
Creates a separate personalized letter for every invitee and saves it in the output folder.
"""



PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as sl:
    letter_content = sl.read()
    for name in names:
        stname = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stname)

        with open(f"./Output/ReadyToSend/letter_for_{stname}.txt", "w") as cl:
            cl.write(new_letter)
