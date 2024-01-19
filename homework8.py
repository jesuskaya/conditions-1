# Task_1

# input_file_name = "input_file.txt"
# input_text = "hello?"
#
# with open(input_file_name, "w", encoding="utf-8") as input_file:
#     input_file.write(input_text)
#
# with open(input_file_name, "r", encoding="utf-8") as input_file:
#     content = input_file.read()
#     words = content.split()
#     filtered_words = [word for word in words if len(word) >= 7]
#
# output_file_name = "new_file.txt"
#
# with open(output_file_name, "w", encoding="utf-8") as output_file:
#     output_file.write(" ".join(filtered_words))
#
# print(output_file_name)  ### почему-то во втором файле ничего не появляется, я уже не знаю что делать, либо я слишком
                           ### намудрил с кодом, либо чего-то не понимаю.


# Task_2

# file_name = "text_file.txt"
# file_content = "This is a text file. We use it to count words."
#
# with open(file_name, "w", encoding="utf-8") as file:
#     file.write(file_content)
#
# with open(file_name, "r", encoding="utf-8") as file:
#     content = file.read()
#     words = content.split()
#     word_count = len(words)
#
# print(f"Word count in the file {file_name}: {word_count}")

#Task_3

# text = """Let me tell you about mv best friend. His name is Yuriy. We have known each other for ages.
# We live in the same town and went to the same school. Now we study at the same university.
# And though we study at different faculties, we see each other almost every day.
# My best friend is the first to come and support me in any difficult situation.
# We have a lot in common. We both do sports regularly.
# That's because we want to be strong and look handsome.
# We really look very much alike. We have short dark hair, grey eyes and a sport figure.
# We also have many similar features of character: we are merry, smart and active."""
#
# forbidden_word = "We"
# replacement = "**"
#
# words = text.split()
# replacement_count = words.count(forbidden_word)
# words = [replacement if word == forbidden_word else word for word in words]
# modified_text = ' '.join(words)
#
# print(modified_text)
# print(f"Replaced '{forbidden_word}' with '{replacement}' {replacement_count} times.")



