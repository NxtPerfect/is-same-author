"""We're not handling the rest of the sentence
it should be saved and used in the next iteration

We only insert space at the front, we don't get any remaining_line in there
and our lines are too short"""

import math
import time

def run(path: str, output: str, author: str, maxWords=50):
    processed_text = ["Text;Author\n"]
    remaining_line = ""
    try:
        print("Start.\nProcessing...")
        with open(path, "r") as file:
            for line in file:
                # time.sleep(1)
                print("Line: " + line)
                line_with_remaining = remaining_line + " " + line
                if remaining_line == '':
                    line_with_remaining = line
                i = -1
                print(f"Counted {line_with_remaining.count(' ')} words and found {line_with_remaining.find('. ')}")
                if line_with_remaining.count(' ') > maxWords and line_with_remaining.find(". ", 1):
                    search_index = len(' '.join(line_with_remaining.split()[:50]))
                    dot = line_with_remaining.find(". ", search_index)
                    if dot == -1:
                        dot = math.inf
                    qmrk = line_with_remaining.find("? ", search_index)
                    if qmrk == -1:
                        qmrk = math.inf
                    xclm = line_with_remaining.find("! ", search_index)
                    if xclm == -1:
                        xclm = math.inf
                    i = min(dot, qmrk, xclm)
                    print("Position is", i)
                    if i == math.inf:
                        remaining_line = line_with_remaining.strip(' \n')
                        continue
                    line_with_remaining = line_with_remaining.replace(";", ",")
                    current_sentence = line_with_remaining[:i+1] + f";{author}\n"
                    processed_text.append(current_sentence)
                    print("Processed line.")
                remaining_line = line_with_remaining[i+1:].strip(' \n')
                print("Saving remaining line.")
        processed_text.append(''.join([remaining_line, f";{author}"]))
        with open(output, "a") as file:
            for line in processed_text:
                file.write(line)
    except IOError as e:
        print(e)
    finally:
        print("\nFinished!")

if __name__ == "__main__":
    run("data.bak/sample2.csv", "data.bak/output2.csv", "Dale Carnegie")
