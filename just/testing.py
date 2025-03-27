#let a robot answer on emotions 
emotion = "=_="
def main():
    global emotion
    speak("is any one there? ")
    robot = input("\n Yes or No \n").strip().title()
    #conditions to test if person is there or not
    if "Yes" in robot:
        emotion = ":D"
        speak("oh great nice to meet you")
    elif "No" in robot:
        emotion = "-_-"
        speak("hmm ok, i guess i'll be off now")
    else:
        emotion = "0-0"
        speak("your responce was wrong Either")
def speak(word):
    print(word + " " + emotion)

#call the function
main()

# list training 
CANS=str(['shige'   ,'kile','kida','rager','fef','tols','form','tom','jack','hope'])
print(CANS)
new = []
for cans in CANS:
    new.append(cans.strip())
print(' '.join(new))
    