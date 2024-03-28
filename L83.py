def replace_substring(main_string, sub_string, rep_string2):
    output = []
    index = 0
    while index < len(main_string):#looking at the main string character by character
        if main_string[index:index+len(sub_string)] == sub_string: #if it equals sub string then (somthing something next character)
            output.append(rep_string2)
            index += len(sub_string)
        else:
            output.append(main_string[index])
            index += 1
    return "".join(output)

string= "something with some words here yay. some yay here. and here is a yay. yay"
sub = "yay"
rep_string = "slay!"
answer = replace_substring(string, sub,rep_string)
print(answer)
