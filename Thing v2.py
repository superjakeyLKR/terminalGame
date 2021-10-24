from bearlibterminal import terminal
from time import sleep as s

def slp(sleepTime): #Time.sleep()s for a specific amount of time (parameter "sleepTime"), then refreshes the terminal.
    terminal.refresh()
    s(sleepTime)

def LoadGame(): #Loads a saved game. (NOT IMPLEMENTED YET)
    terminal.color(terminal.color_from_name("narratorColor"))
    terminal.printf(0, 0, "Sorry, but loading hasn't been implemented yet :(.")
    slp(1)
    terminal.printf(0, 0, " " * 60)
    terminal.printf(0, 1, " " * 4)
    Start()

def Start(): #The stuff that happenes at the start of the game.
    i = 0
    name = " "
    backstory = ["Now, you may wonder why you're here.", "Or where exactly \"here\" is.", "All will be answered in due time.",
                "But first, there is something that needs to be done.",
                "A curse, as old as time itself, has wreaked havoc on this world for long enough.",
                "It's up to you to fight the curse and free these people.", "Your quest starts here, in an... unlikely place"]
    terminal.open()
    terminal.printf(0, 0, "Enter name: ")
    terminal.set("window.title = Enter your name.; palette: playerColor = #c2ffff, narratorColor = white")
    terminal.color(terminal.color_from_name("playerColor"))
    terminal.refresh()

    while True: #Gets the name of the player
        key = terminal.read()
        if key != terminal.TK_RETURN:
            name += chr(key + 93)
            terminal.put(i, 1, chr(key + 93))
            i += 1
            terminal.refresh()
        else:
            name = name.title()
            break
    
    if name == " Load":
        LoadGame()
    elif name == " Skipone":
        terminal.color(terminal.color_from_name("narratorColor"))
        terminal.printf(0, 0, "[bkcolor=blue]Chapter 1: The Start[/bkcolor][bkcolor=black]")
        ChapterOne(" Test") 
    terminal.set("window.title = The Backstory.")
    terminal.color(terminal.color_from_name("narratorColor"))
    terminal.printf(0, 0, "[bkcolor=darker purple]Hello,{}.[/bkcolor]  ".format(name))
    terminal.printf(0, 1, " " * len(name))
    slp(1)

    i = 1
    while i <= len(backstory): #Prints the backstory
        terminal.printf(0, i, backstory[i - 1])
        i += 1
        slp(1)

    terminal.printf(0, len(backstory) + 1, "[bkcolor=blue]Chapter 1: The Start[/bkcolor]")
    slp(2)

    i = len(backstory)
    while i >= 0: #Does the cool title thing.
        terminal.printf(0, i + 1, "[bkcolor=black]" + " " * 80 + "[/bkcolor]")
        terminal.printf(0, i, "[bkcolor=blue]Chapter 1: The Start[/bkcolor][bkcolor=black]" + " " * 60 + "[/bkcolor]")
        #The end bit is just to make sure that the whole line is cleared.
        i -= 1
        slp(0.2)

    slp(1)
    ChapterOne(name)

def ChapterOne(name):
    name = name
    i = 1
    startText = ["You wake up after a long night's rest, startled by the dream you just had.",
                "[color=playerColor]\"What, or, more importantly, who was that voice?\" [color=narratorColor]you say,[color=playerColor] \"Curses? A quest?\"",
                "You get up, and look at yourself in the mirror.",
                "[color=playerColor]\"Me,{}? Why would I be the person to do this? There are [color=lighter playerColor]WAY[color=playerColor] more capable".format(name),
                "[color=playerColor]people than me to do this!\"",
                "But, before you could even react, you door gets barged down.",
                "[color=dark red]ThErE hE iS!!! gEt HiM!!!",
                "[color=playerColor]\"Who the hell are...\"",
                "Before you could finish the sentence, you get knocked out by the invadors."]
    kidnappedText = ["...", "." * 6, "." * 9, "." * 12,
                    "[color=dark red]ArE wE tHeRe YeT?",
                    "[color=darker red]No.",
                    "...", "[color=dark red]HoW aBoUt NoW?",
                    "[color=darker red]StIlL nO.",
                    "...", "[color=dark red]NoW?",
                    "[color=darker red]I sWeAr If YoU aSk Me OnE mOrE tImE i WiLl LoSe It.",
                    "...", "." * 6, "[color=dark red]aRe We ThErE...",
                    "[color=narratorColor]You hear the sound of someone being forcefully kicked of the side of what",
                    "[color=narratorColor]seems to be a bridge.",
                    "[color=darker red]ThE iRoNiC tHiNg Is ThAt We HaVe JuSt ArRiVeD aT OuR DeStInAtIoN.",
                    "[color=narratorColor]You hear a voice welcoming you to [color=dark red]\"PaUiRtGdY\"[/color][color=narratorColor]."]
    pauirtgdyText = ["When you wake up, you are in, what seems to be, a royal palace.",
                    "A rather [color=blue]wet[/color] royal palace.",
                    "[color=light orange]So, We FiNaLlY mEt AgAin At LaSt!",
                    "You look around, trying to see where the voice is coming from.",
                    "[color=light orange]DoWn hErE, sTuPiDo.",
                    "You look to see a small, fish-looking sphere with a yellow hat on.",
                    "[color=light orange]So, ArE yOu ReAdY tO pAy?!?",
                    "[color=playerColor]\"Pay for what?\" [/color]you ask the weird-looking creature.",
                    "[color=light orange]YOUR CRImes...",
                    "It looks at you with both anger and confusion.",
                    "He calls out a name, and another, similar creature walk into the room",
                    "[color=light orange]WhO tHe HeLl Is ThIs? DiD yOu NoT rEaD tHe WaNtEd PoStEr?",
                    "[color=darker red]I cAn'T rEaD.",
                    "[color=light orange]WhErE iS tHe OtHeR gUy? CaN't He ReAd?",
                    "[color=darker red]I kIcKeD hIm Of ThE sIdE oF tHe BrIdGe.",
                    "[color=light orange]WHAT DID YOU DO THAT FOR?",
                    "[color=darker red]He WaS aNnOyInG mE a LoT, sO i GoT rId oF hIm.",
                    "[color=light orange]I sWeAr It'S [color=orange]IMPOSSIBLE[color=light orange] tO gEt GoOd hElP nOwAdAys.",
                    "[color=light orange]YoU! hUmaN! tElL mE yOuR nAmE!"
                    "You tell the creature that is it[color=playerColor]{}.".format(name),
                    "[color=light orange]So,{}, sOrRy fOr, YoU kNoW, kIdNaPpInG yOu AnD aLl.".format(name)]
    terminal.set("window.title = Chapter 1: The Start.")

    while i <= len(startText):
        terminal.printf(0, i, startText[i - 1])
        slp(0.5)
        i += 1
    
    terminal.clear()
    terminal.printf(0, 0, "[bkcolor=blue]Chapter 1.1: A... Turbulent Begining.[/bkcolor]")
    terminal.set("window.title = Chapter 1.1: A... Turbulent Begining.")
    slp(2)
    i = 1
    terminal.color(terminal.color_from_name("playerColor"))
    while i <= len(kidnappedText):
        terminal.printf(0, i, kidnappedText[i - 1])
        slp(0.5)
        i += 1
    slp(1)
    terminal.color(terminal.color_from_name("narratorColor"))
    terminal.clear()
    terminal.printf(0, 0, "[bkcolor=blue]Chapter 1.2: Welcome to \"PaUiRtGdY\".[/bkcolor]")
    terminal.set("window.title = Chapter 1.2: Welcome to \"PaUiRtGdY\".")
    slp(2)
    i = 1
    while i <= len(pauirtgdyText):
        terminal.printf(0, i, pauirtgdyText[i - 1])
        slp(1)
        if i == 3:
            terminal.set("window.title = YOU WILL PAY.")
        elif i == 11:
            terminal.set("window.title = Sorry, Wrong Person.")
        i += 1
    terminal.close()



if __name__ == "__main__": #Obligatory 'if __name__ == "__main__":'
    Start()                #thing to let people who are good at coding
                           #know that you are supposed to run this script.
