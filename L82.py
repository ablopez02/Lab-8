def remove_substring(main_string, sub_string):
    output = []
    index = 0
    while index < len(main_string):
        if main_string[index:index+len(sub_string)] == sub_string:
            index += len(sub_string)
        else:
            output.append(main_string[index])
            index += 1
    return "".join(output)
string= "something with some words here yay. some yay here. and here is a yay. yay"
sub = "yay"
answer = remove_substring(string, sub)
print(answer)
