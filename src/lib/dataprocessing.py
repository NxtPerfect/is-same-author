"""Open file and read it line by line
then if the line has more than 50 words, we insert comma, the author and new line
if the line has less than that, we should remove new line from the end of it
and add it to the next line, and divide it

However, if we're reading it line by line, it won't ever have a new line in the end
and we'll end up with 'line' being another line, which will never join them together

One solution is to use stack, if line is shorter we add it in, then we join them together
and change file at index of first line till last line to that one line we created

additionally we're only finding . but we should also look for ! and ?"""

# file = open("data.bak/sample1.csv", "r+")
file = open("data.bak/test.csv", "r+")
stack = []
try:
    data = file.readlines()
    for idl, line in enumerate(data):
        i = -1
        # count how many words
        # if more than 250 then put new line at next coma
        if line.count(' ') >= 50 and line.find(",Timothy Ferris\n") != -1:
            i = line.find(". ")
            line = line[:i] + ",Timothy Ferriss\n" + line[i:]
            data[idl] = line
            print("Adding author at char " + str(i) + ".")
            continue
        # while stack is not empty
        # then join lines
        if line.find(",Timothy Ferris\n") != -1:
            print("Found author " + str(idl+1))
            print(line)
            continue
        if line.count(' ') < 50 and stack:
            # check if line + lines from stack > 50
            # then join them
            # find . ! ? and split them there
            # write first line to file at index of stack line
            # if added to stack, remove from file
            pass
        if line.count(' ') < 50:
            print("Line too short " + str(idl+1))
            print(line)
            stack.append((idl, line))
            continue
        print("Other type of error, maybe line too long " + str(idl+1))
except IOError:
    file.close()
finally:
    file.close()
