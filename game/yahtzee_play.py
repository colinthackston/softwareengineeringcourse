from yahtzee_lib import *
import tkinter as tk
from PIL import Image
import time
import socket, errno
from time import sleep
import threading
from network import Network


class Player:
    def __init__(self, currScore, highScore):
        self.currScore = currScore
        self.highScore = highScore

    def update(self):
        self.currScore = self.currScore
        self.highScore = self.highScore


def play():
    root = tk.Tk()
    global network1
    network1 = Network()
    global player1
    player1 = Player(0, 0)
    global player2
    player2 = Player(0, 0)
    p1tkscore = tk.IntVar(root)
    p2tkscore = tk.IntVar(root)
    p1tkscore.set(player1.currScore)
    p2tkscore.set(player2.currScore)
    network1.send(str(p1tkscore))
    print("playing")

    root.configure(bg="#00008B")
    prev_caller = ()
    turns_done = 0
    top_banner = tk.Label(root, text="Your score:  ", width=20, height=1).grid(
        row=1, column=3
    )
    second_banner = tk.Label(root, text="Player2 score:  ", width=20, height=1).grid(
        row=1, column=5
    )
    make_dice()
    thrkind, frkind, full, smll, lrg, yaht, chan = (), (), (), (), (), (), ()
    one, two, three, four, five = (), (), (), (), ()
    score_ = tk.IntVar(root)
    score_.set(0)

    score_show = tk.Label(root, textvariable=p1tkscore, width=20, height=1).grid(
        row=1, column=4
    )
    score_show_p2 = tk.Label(root, textvariable=p2tkscore, width=20, height=1).grid(
        row=1, column=6
    )

    def end_game():
        nonlocal score_
        score_final = score_.get()
        root.destroy()
        over_window = tk.Tk()
        congradulations = tk.Label(
                over_window, text="Congratulations you win! your score was:  "
            ).grid(row=1, column=1)
        done_score = tk.Label(over_window, text=p1tkscore).grid(row=1, column=2)

    def change(die):
        if die.hold == False:
            hold(die)
        elif die.hold == True:
            unhold(die)
        update()

    def is_held(die):
        if die.hold == False:
            return ""
        elif die.hold == True:
            return "   Hold"
        update()

    def update():
        nonlocal dice1_
        nonlocal dice2_
        nonlocal dice3_
        nonlocal dice4_
        nonlocal dice5_
        nonlocal dice1
        nonlocal dice2
        nonlocal dice3
        nonlocal dice4
        nonlocal dice5

        dice1_ = str(str(dice.dice_exist[0].value) + is_held(dice.dice_exist[0]))
        dice2_ = str(str(dice.dice_exist[1].value) + is_held(dice.dice_exist[1]))
        dice3_ = str(str(dice.dice_exist[2].value) + is_held(dice.dice_exist[2]))
        dice4_ = str(str(dice.dice_exist[3].value) + is_held(dice.dice_exist[3]))
        dice5_ = str(str(dice.dice_exist[4].value) + is_held(dice.dice_exist[4]))

        dice1.set(dice1_)
        dice2.set(dice2_)
        dice3.set(dice3_)
        dice4.set(dice4_)
        dice5.set(dice5_)

        print(dice1.get())
        print(dice2.get())
        print(dice3.get())
        print(dice4.get())
        print(dice5.get())

    dice1 = tk.StringVar(root)
    dice2 = tk.StringVar(root)
    dice3 = tk.StringVar(root)
    dice4 = tk.StringVar(root)
    dice5 = tk.StringVar(root)

    dice1_ = str(str(dice.dice_exist[0].value) + is_held(dice.dice_exist[0]))
    dice2_ = str(str(dice.dice_exist[1].value) + is_held(dice.dice_exist[1]))
    dice3_ = str(str(dice.dice_exist[2].value) + is_held(dice.dice_exist[2]))
    dice4_ = str(str(dice.dice_exist[3].value) + is_held(dice.dice_exist[3]))
    dice5_ = str(str(dice.dice_exist[4].value) + is_held(dice.dice_exist[4]))

    dice1.set(dice1_)
    dice2.set(dice2_)
    dice3.set(dice3_)
    dice4.set(dice4_)
    dice5.set(dice5_)

    dice_1 = tk.Button(
        root,
        textvariable=dice1,
        width=20,
        height=1,
        command=lambda: change(dice.dice_exist[0]),
    ).grid(column=2, row=2)
    dice_2 = tk.Button(
        root,
        textvariable=dice2,
        width=20,
        height=1,
        command=lambda: change(dice.dice_exist[1]),
    ).grid(column=3, row=2)
    dice_3 = tk.Button(
        root,
        textvariable=dice3,
        width=20,
        height=1,
        command=lambda: change(dice.dice_exist[2]),
    ).grid(column=4, row=2)
    dice_4 = tk.Button(
        root,
        textvariable=dice4,
        width=20,
        height=1,
        command=lambda: change(dice.dice_exist[3]),
    ).grid(column=5, row=2)
    dice_5 = tk.Button(
        root,
        textvariable=dice5,
        width=20,
        height=1,
        command=lambda: change(dice.dice_exist[4]),
    ).grid(column=6, row=2)

    hand_val = tk.IntVar(root)
    hand_val.set(0)
    hand_texthelper = tk.Label(root, text="Your Hand Value:", width=20, height=1).grid(
        row=3, column=3
    )
    hand_value = tk.Label(root, textvariable=hand_val, width=20, height=1).grid(
        row=3, column=4
    )

    def hand_val_changer(amount, caller):
        nonlocal hand_val
        nonlocal prev_caller
        hand_val.set(amount)
        prev_caller = caller
        update()

    aa = tk.StringVar(root)
    aa.set("Ones")
    ab = tk.StringVar(root)
    ab.set("Twos")
    ac = tk.StringVar(root)
    ac.set("Threes")
    ad = tk.StringVar(root)
    ad.set("Fours")
    ae = tk.StringVar(root)
    ae.set("Fives")
    af = tk.StringVar(root)
    af.set("Sixes")
    ag = tk.StringVar(root)
    ag.set("Three of a Kind")
    ah = tk.StringVar(root)
    ah.set("Four of a Kind")
    ai = tk.StringVar(root)
    ai.set("Full House")
    aj = tk.StringVar(root)
    aj.set("Small Straight")
    ak = tk.StringVar(root)
    ak.set("Large Straight")
    al = tk.StringVar(root)
    al.set("Yahtzee")
    am = tk.StringVar(root)
    am.set("Chance")

    one = tk.Button(
        root,
        textvariable=aa,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((ones() * 1), "one"),
    ).grid(column=1, row=4)
    two = tk.Button(
        root,
        textvariable=ab,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((twos() * 2), "two"),
    ).grid(column=2, row=4)
    three = tk.Button(
        root,
        textvariable=ac,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((threes() * 3), "three"),
    ).grid(column=3, row=4)
    four = tk.Button(
        root,
        textvariable=ad,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((fours() * 4), "four"),
    ).grid(column=4, row=4)
    five = tk.Button(
        root,
        textvariable=ae,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((fives() * 5), "five"),
    ).grid(column=5, row=4)
    six = tk.Button(
        root,
        textvariable=af,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((sixes() * 6), "six"),
    ).grid(column=6, row=4)

    thrkind = tk.Button(
        root,
        textvariable=ag,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((three_of_kind()), "thrkind"),
    ).grid(column=1, row=5)
    frkind = tk.Button(
        root,
        textvariable=ah,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((four_of_kind()), "frkind"),
    ).grid(column=2, row=5)
    full = tk.Button(
        root,
        textvariable=ai,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((full_house()), "full"),
    ).grid(column=3, row=5)
    smll = tk.Button(
        root,
        textvariable=aj,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((sm_straight()), "smll"),
    ).grid(column=4, row=5)
    lrg = tk.Button(
        root,
        textvariable=ak,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((lrg_straight()), "lrg"),
    ).grid(column=5, row=5)
    yaht = tk.Button(
        root,
        textvariable=al,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((yahtzee()), "yaht"),
    ).grid(column=6, row=5)
    chan = tk.Button(
        root,
        textvariable=am,
        width=(20),
        height=1,
        command=lambda: hand_val_changer((chance()), "chance"),
    ).grid(column=7, row=5)

    buttons = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "thrkind",
        "frkind",
        "full",
        "smll",
        "lrg",
        "yaht",
        "chance",
    ]

    def selector():
        nonlocal hand_val
        nonlocal score_
        nonlocal prev_caller
        nonlocal buttons
        nonlocal one
        nonlocal two
        nonlocal three
        nonlocal four
        nonlocal five
        nonlocal six
        nonlocal thrkind
        nonlocal frkind
        nonlocal full
        nonlocal smll
        nonlocal lrg
        nonlocal yaht
        nonlocal chan

        if prev_caller == "one":
            if "one" in buttons:
                buttons.remove("one")
                aa.set("Used Already")
                return True

        if prev_caller == "two":
            if "two" in buttons:
                buttons.remove("two")
                ab.set("Used Already")
                return True
        if prev_caller == "three":
            if "three" in buttons:
                buttons.remove("three")
                ac.set("Used Already")
                return True
        if prev_caller == "four":
            if "four" in buttons:
                buttons.remove("four")
                ad.set("Used Already")
                return True
        if prev_caller == "five":
            if "five" in buttons:
                buttons.remove("five")
                ae.set("Used Already")
                return True
        if prev_caller == "six":
            if "six" in buttons:
                buttons.remove("six")
                af.set("Used Already")
                return True
        if prev_caller == "thrkind":
            if "thrkind" in buttons:
                buttons.remove("thrkind")
                ag.set("Used Already")
                return True
        if prev_caller == "frkind":
            if "frkind" in buttons:
                buttons.remove("frkind")
                ah.set("Used Already")
                return True

        if prev_caller == "full":
            if "full" in buttons:
                buttons.remove("full")
                ai.set("Used Already")
                return True
        if prev_caller == "smll":
            if "smll" in buttons:
                buttons.remove("smll")
                aj.set("Used Already")
                return True
        if prev_caller == "lrg":
            if "lrg" in buttons:
                buttons.remove("lrg")
                ak.set("Used Already")
                return True
        if prev_caller == "yaht":
            if "yaht" in buttons:
                buttons.remove("yaht")
                al.set("Used Already")
                return True
        if prev_caller == "chance":
            if "chance" in buttons:
                buttons.remove("chance")
                am.set("Used Already")
                return True
        else:
            return False

    def choose():
        nonlocal turns_done
        nonlocal end_game
        if turns_done == 12:
            end_game()
        if selector() == True:
            help = p1tkscore.get() + hand_val.get()
            p1tkscore.set(help)
            requestedScore = network1.send(str(p1tkscore))

            p2tkscore.set(requestedScore)

            rolls_left.set(3)
            turns_done += 1
            Canroll.set("Roll")
            for item in dice.dice_exist:
                item.hold = False
            roll_()
            update()

        else:
            return False

    confirm = tk.Button(
        root,
        text="Confirm Hand Selection",
        width=20,
        height=1,
        command=lambda: choose(),
    ).grid(column=4, row=6)

    Canroll = tk.StringVar(root)
    Canroll.set("Roll")

    rolls_left = tk.IntVar(root)
    rolls_left.set(2)

    def roll_():
        nonlocal rolls_left
        nonlocal Canroll
        if rolls_left.get() > 0:
            roll()
            rolls_left.set(rolls_left.get() - 1)
        if rolls_left.get() == 0:
            Canroll.set("Must Choose")
        update()

    roller = tk.Button(
        root, textvariable=Canroll, width=20, height=1, command=lambda: roll_()
    ).grid(column=4, row=7)
    rolls_remaing_seter = tk.Label(
        root, text="Rolls Remaining:  ", width=20, height=1
    ).grid(column=2, row=7)
    rolls_remaining = tk.Label(root, textvariable=rolls_left, width=20, height=1).grid(
        column=3, row=7
    )

    roll()
    update()

    root.mainloop()
