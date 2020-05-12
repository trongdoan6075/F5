# This method is to get the longest length of the word from the list.
def getlongestword(str):
    temp = 0
    string = ''
    list = str.split(" ")
    for word in list:
        if len(word) > temp:
            temp = len(word)
            string = word
    return string

# This method is to print the name of the avatar that is showing on the page.
# Base on the mapping hash created, name will be printed accordingly
def printAvatarName(list):
    hash = {"https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg": "Mario",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg": "Robot",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg": "Punisher",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg": "BATMAN",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-6.jpg": "Star War",
            "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg": "Circus Man"}
    counter = 1
    for i in range(0, len(list)):
        for k, v in hash.items():
            if list[i] == k:
                print(str(counter) + ". " + "Avatar's Name: " + v)
                counter += 1

# This method is to check if the Punisher is shown on the page or not.
# return True if it shows, otherwise return False
def checkPunisherdisplay(list):
    target_silhouette = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"

    for i in range(0, len(list)):
        if list[i] == target_silhouette:
            return True

    print("Punisher Avartar did not show up in the page.")
    return False