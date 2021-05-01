placeholder="[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names= names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        result=letter_contents.replace(placeholder, stripped_name)
        print(result)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as compeleted_letter:
            compeleted_letter.write(result)

