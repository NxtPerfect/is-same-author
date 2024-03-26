"""Open file and read it line by line
then if the line has more than 50 words, we insert comma, the author and new line
if the line has less than that, we should remove new line from the end of it
and add it to the next line, and divide it

However, if we're reading it line by line, it won't ever have a new line in the end
and we'll end up with 'line' being another line, which will never join them together

One solution is to use stack, if line is shorter we add it in, then we join them together
and change file at index of first line till last line to that one line we created

additionally we're only finding . but we should also look for ! and ?"""

# file = open("data.bak/sample1.csv")
file = """this is some sample data
that i'm testing python in
and we should really see
how long it can go
and if this line gets too long then it should divide it. Now if we found another thing then
we should divide it in another spot which should be somewhere nearby. That means we have at least
three sentences now and it should try and change it at least once, i think so no?
what about exclamation marks! or question marks? it won't find them
exactly."""
stack = []
for idl, line in enumerate(file):
    newline = False
    i = -1
    # count how many words
    # if more than 250 then put new line at next coma
    if line.count(" ") > 50:
        i = line.find(".")
        line = line[:i+1] + ",Jim Bim\n" + line[i+1:]
        newline = False
        print("Adding author")
        continue
    # while stack is not empty
    # then join lines
    stack.append((idl, line))
    print("Too long line")
