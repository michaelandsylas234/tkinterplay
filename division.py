
def suffix(number):
    if number==1: return "st"
    elif number==2: return "nd"
    elif number==3: return "rd"
    else: return "th"

text = input("Type a fraction> ")  # Python 3
tokens = text.rsplit('/')
if len(tokens) != 2:
    print ("That isn't a fraction! Please reopen this PyThon script.")
    key = input('Press Enter to continue...')
    quit()

else:   
    numerator = int(tokens[0])
    denominator = int(tokens[1])

    print ("The numerator is "  + str(numerator))
    print ("The denominator is " + str(denominator))

    # first lets break up the numerator into digits ie 475 => [4, 7, 5].
    numerator_stream = []
    while numerator != 0:
        numerator_stream.append(numerator % 10)
        numerator = int(numerator / 10)  # rounds down

    numerator_stream.reverse()

    accumulator = 0
    memory = []   # all of the values of the accumulator seen before - used for cycle detection
    answer = []
    decimal_place_location = len(numerator_stream)
    repeats_at = -1

    step = 1
    while True:
        if len(numerator_stream) == 0 and accumulator == 0:
            break

        # pick the first digit off of the numerator_stream
        print ("STEP", step, ":")
        if (len(numerator_stream) == 0):
            print (" (writing a zero on the end of the numerator!)")
            numerator_stream.append(0)
        print ("  ANSWER SO FAR:", answer)
        print ("  NUMERATOR:", numerator_stream)
        print ("  REMAINDER:", accumulator)

        digit = numerator_stream.pop(0) # removes the first digit
        print ("  -- pull down", digit, "and add to 10×" + str(accumulator))
        accumulator = 10 * accumulator + digit
        print ("  -- new accumulator is", accumulator)

        if (accumulator in memory):
            print ("  -- we have found a cycle!")
            repeats_at = memory.index(accumulator)
            break
        else:
            memory.append(accumulator)
            nextdigit = 0
            for trydigit in range(9):
                product = trydigit * denominator
                print("  ---- trying " + str(trydigit) + "×" + str(denominator) + "... The answer is " + str(product) + ". Comparing to " + str(accumulator) + "...")
                if product <= accumulator:
                    nextdigit = trydigit
                else:
                    break
        
        answer.append(nextdigit)
        accumulator = accumulator - nextdigit * denominator
        step = step + 1


print("The answer is " + str(answer) + ".  The decimal place is after the " + str(decimal_place_location) + suffix(decimal_place_location) + " digit.")
if (repeats_at > 0):
     print("it repeats starting at the ", repeats_at, "digit")
else:
    print ("it doesn't repeat")

print ("now lets print the answer the right way")
numberstring = ""

digit = 0
for d in answer:
    if (len(numberstring) == 0 and d == 0 and digit != decimal_place_location):
        print("ignore a zero in the front")
    else:
        if (digit == decimal_place_location):
            numberstring = numberstring + "."
        numberstring = numberstring + str(d)
    digit = digit + 1

print ("the answer is", numberstring)
if repeats_at >= 0:
    print ("it starts repeating at the ", repeats_at-decimal_place_location+1, " digit")
    
key = input('Press Enter to continue...')
quit()


    


    

