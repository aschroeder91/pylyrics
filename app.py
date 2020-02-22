from random import randint
rand = randint(1, 4)
try:
    fhand1 = open("Lyrics" + str(rand) + ".txt")
except:
    fhand1 = open(input("enter file name: ") + ".txt")

lyricslist = []  # making the list
for lines in fhand1:
    lines = lines.lower()
    lines = lines.replace("-", " ")
    lines = lines.replace("'", "")
    lines = lines.replace(",", "")
    lyricslist += lines.split()
    lyricslist += " "

aartist = lyricslist.index("artist:") + 1
atitle = lyricslist.index("title:") + 1
ptitle = lyricslist.index(" ", atitle, 20)
artist = " ".join(lyricslist[aartist:atitle - 2])
title = " ".join(lyricslist[atitle:ptitle])

answer = title.title() + " by " + artist.title()
print(answer)
print("Lyrics:")


def songfinish():
    base = ""
    while base != "exit":
        base = input(">: ").lower()
        base = base.replace("'", "")
        ppos = -1
        apos = -1
        if base == artist or base == title:
            print(answer)
            print("CONGRATS! you win!")
            break
        elif base not in lyricslist:
            continue
        elif base == 'the' or base == 'a' or base.isnumeric() or base == 'and' or base == 'or':
            print("...")
        else:
            apos = lyricslist.index(base)
            ppos = lyricslist.index(" ", apos, 500)
            output = " ".join(lyricslist[apos + 1:ppos])
            print(output + "?")


songfinish()
