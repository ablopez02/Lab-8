#the join adds seperated strings together
line = ["Haiku rogs in snow",
        "A limerick came from Nantucket",
        "Tetrameteric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(string_list):
    return "<br>".join(string_list)
print(breakify(line))



string= "hello world!"
output = []#empty list
index = 0
while index < len(string):
    output.append(string[index])#using th append character
    index += 1# this will move to the next character
print(output)



string = 'SPAM!HelloSPAM! worldSPAM!!'
output = []
index = 0
while index < len(string):
    if string[index:index+5] == 'SPAM1' :
        index += 5
    else:
        output.append(string[index])
        index += 1

print("".join(output))


