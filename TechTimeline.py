#!/usr/bin/python
#TechTimeline.py
__version__ = "1.0"
__author__ = 'beckwith'


import tkinter
from tkinter.font import Font

# open up pdf with list of inventions:
import subprocess
subprocess.call(['open', "problems.pdf"])

# root tkinter window for all graphics
root = tkinter.Tk() 
root.title("TECH TIMELINE GAME")  

# encrypted:
PROBLEMS = {
    " 1. monitor"      :-994901968,
    " 2. touch screen" :-994828258,
    " 3. desktop"      :-994894597,
    " 4. programmable" :-995115727,
    " 5. Mac"          :-994879855,
    " 6. mouse"        :-994924081,
    " 7. smart phone"  :-994651354,
    " 8. email"        :-994916710,
    " 9. laptop"       :-994843000,
    "10. comp w/sound" :-994813516,
    "11. handheld games":-994857742,
    "12. LCD monitors"  :-994739806,
    "13. keyboard"      :-994887226,
    "14. dumb cellphone":-994901968,
    "15. transistor"    :-995042017,
    "16. CPUs"          :-994916710,
    "17. RAM"           :-994938823,
    "18. Google"        :-994717693,
    "19. Amazon"        :-994747177,
    "20. Facebook"      :-994673467,
    "21. browser"       : -994776661,
    "22. text adv."     :-994879855,
    "23. first vid game":-994983049,
    "24. GUI"           :-994901968,
    "25. music player"   :-994725064,
    "26. word proc."     :-994857742,
    "27. USB"            :-994732435,
    "28. network"        :-994931452,
    "29. calculator"     :-994946194,
    "30. sci. calculator":-994909339,
    "31. graphing calc.":-994813516,
    "32. Tetris"        :-994820887,
    "33. Angry Birds"   :-994636612,
    "34. World of Warcraft":-994673467,
    "35. Minecraft"    :-994636612,
    "36. Pong"         :-994909339,
    "37. Fortnite"     :-994577644,
    "38. Play Station" :-994747177,
    "39. PacMan"       :-994850371,
    "40. Legend of Zelda":-994806145,
    "41. Mario Bros."   :-994828258,
    "42. Asteroids"     : -994857742
    }
#DEBUG:
#PROBLEMS = {"39. PacMan"       :-994850371,     "37. Fortnite"     :-994577644}
# get list of inventions/keys:
inventions = list(PROBLEMS.keys()) 
# corresponding list of years:
years_ct      = list(PROBLEMS.values()) 

vals = [False for i in range(len(inventions))]
got_right = dict(zip(inventions, vals))

player_score = 1000

num_decades  = 8
start_decade = 1940

# for timer score:
started = False 
time = 0

#2D array of lists of choices in each decade
choices = []  

correct_decade = 0 # for scoring purposes


def quitting_time():
    '''called when Quit button is pressed'''
    root.destroy()
    
    
def submit():
    '''called when the submit button is clicked - check all answers and update things'''
    global player_score, t, correct_decade
    player_score -= 50
    total_score_var.set("Total Score: " + str(player_score))    
    # go through each decade
    for i in range(num_decades):
        # go through each choice in the list and see if year matches:
        for c in choices[i]:
            val  = str(PROBLEMS[c])                # the year
            srch = str(start_decade + 10 * i)[:3]  # first 3 digits of year
            if val.find(srch) != -1 and not got_right[c]:               # found, so correct decade
                correct_decade += 1
                player_score += 100
                got_right[c] = True

    # display score and correct count
    old_score = int(score_var.get()[8:]) + 1  # removes "ROUNDS: "
    score_var.set("ROUNDS: " + str(old_score))
    
    decade_var.set("CORRECT DECADE: " + str(correct_decade)  + " of " + str(len(PROBLEMS)))

    if correct_decade == len(PROBLEMS):
        root.after_cancel(t)
    
def timer():
    '''show time elapsed'''
    global time, player_score, t
    time += 1
    if time % 2 == 0:
        player_score -= 1
    total_score_var.set("Total Score: " + str(player_score))
    mins = str(time // 60)
    secs = str(time % 60)
    if len(secs) == 1:
        secs = "0" + secs
    time_var.set("TIME: " + mins + ":" + secs)
    t = root.after(1000, timer)


def check(i):
    '''menu item selected so add/subtract item from appropriate displays/lists'''
    global started, player_score
    
    if not started:
        started = True
        player_score = 1000
        timer()

    selection = menu_vars[i].get()
    
    found_location = -1
    # find if any list already has choice - if so, remove it
    for j in range(len(choices)): # go through each decade
        for c in choices[j]:      # go through list of events in decade
            if c == selection:
                #remove from the list:
                choices[j].remove(selection)
                # so that you can remove an item from the current display:
                found_location = j 
                #remove from display:
                start = results_list[j].find(selection)
                end   = results_list[j].find("\n", start + 1)
                results_list[j] = results_list[j][0:start] + results_list[j][end + 1:]

                results_displays[j].configure(state="normal") # allow editing of text
                results_displays[j].delete(1.0, tkinter.END)
                results_displays[j].insert(tkinter.END, results_list[j]) # show results in text area
                results_displays[j].configure(state="disabled") # prevent editing of text#
                #slice results_list[j] to get rid of
    
    # add to list and display:
    if found_location != i and selection != "SELECT:":
        choices[i].append(selection)
        results_list[i] += selection +"\n"
    
    results_displays[i].configure(state="normal") # allow editing of text
    results_displays[i].delete(1.0, tkinter.END)
    results_displays[i].insert(tkinter.END, results_list[i]) # show results in text area
    results_displays[i].configure(state="disabled") # prevent editing of text#
    
    
# SET UP ALL THE DISPLAY COMPONENTS:
my_font = Font(family="Helvetica", size=14, weight="bold")
decade_font = Font(family="Helvetica", size=15, weight="bold")

# Text displays for lists below menus:
results_displays = []
results_list     = []

for i in range(num_decades):
    
    results_display = tkinter.Text(root,  
                        height=12,
                        relief = "ridge",
                        bd = 6, 
                        width=26,
                        font=my_font,
                        foreground='white',
                        background='black')
    results_display.configure(state="disabled")
    results_display.config(wrap=tkinter.WORD)
    results_displays.append(results_display)
    results_list.append("")
    
    choices.append([])

#  BUTTONS
submit_button = tkinter.Button(text = "CHECK ANS", command = submit, padx=10, pady=3)
quit_button = tkinter.Button(root, text="Quit", command=quitting_time, padx=10, pady=3)

# create the optionmenu (pulldown menu) with the options above:
option_menus = []
menu_vars    = []

OPTIONS = ["SELECT:"] + inventions

# NOTE - COULDN'T SOLVE the problem of check(i) sending menu item, not index
#  so had to forgo a loop here
#0
menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[0], 
                                 *OPTIONS, command = lambda x: check(0))
option_menus.append(option_menu)

#1
menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[1], 
                                 *OPTIONS, command = lambda x: check(1))
option_menus.append(option_menu)

#2
menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[2], 
                                 *OPTIONS, command = lambda x: check(2))
option_menus.append(option_menu)

#3

menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[3], 
                                 *OPTIONS, command = lambda x: check(3))
option_menus.append(option_menu)
#4

menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[4], 
                                 *OPTIONS, command = lambda x: check(4))
option_menus.append(option_menu)
#5

menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[5], 
                                 *OPTIONS, command = lambda x: check(5))
option_menus.append(option_menu)
#6

menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[6], 
                                 *OPTIONS, command = lambda x: check(6))
option_menus.append(option_menu)
#7

menu_var = tkinter.StringVar(root)
menu_var.set(OPTIONS[0]) # default value
menu_vars.append(menu_var)

option_menu = tkinter.OptionMenu(root, menu_vars[7], 
                                 *OPTIONS, command = lambda x: check(7))
option_menus.append(option_menu)

for key, value in PROBLEMS.items():
    pt = round(((value - 2623400) / 567 + 1784953) / 13)
    PROBLEMS[key] = pt
    
# place all labels and menus in root window:
for i in range(num_decades):
    decade_str = str(start_decade + i * 10) + "'s"
    if i < 4:
        tkinter.Label(root, text=decade_str, 
                      font=("Helvetica", "18", "bold")).grid(row=1, column=i, columnspan=1)
        option_menus[i].grid(    row=2, column=i, columnspan=1)
        results_displays[i].grid(row=3, column=i, columnspan=1)
    else:
        tkinter.Label(root, text=decade_str, 
                      font=("Helvetica", "18", "bold")).grid(row=4, column=i % 4, columnspan=1)        
        option_menus[i].grid(    row=5, column=i % 4, columnspan=1)
        results_displays[i].grid(row=6, column=i % 4, columnspan=1)
   



submit_button.grid(row=0, column=2, columnspan=1)
quit_button.grid(  row=0, column=3, columnspan=1)
submit_button.config(font=('Verdana', '20'))
quit_button.config(font=('Verdana', '20'))

score_var = tkinter.StringVar(root)
score_var.set("ROUNDS: 0")
score_lbl = tkinter.Label(root, textvariable=score_var, fg="blue")
score_lbl.config(font=('Verdana', '20'))
score_lbl.grid(row=0, column=1, columnspan=1)

time_var = tkinter.StringVar(root)
time_var.set("TIME: 0:00")
time_lbl = tkinter.Label(root, textvariable=time_var, fg="red")
time_lbl.config(font=('Verdana', '20'))
time_lbl.grid(row=0, column=0, columnspan=1)

decade_var = tkinter.StringVar(root)
decade_var.set("CORRECT DECADE: 0")
decade_lbl = tkinter.Label(root, 
                           textvariable=decade_var, 
                           fg="red",  
                           bg="black",
                           font=decade_font,
                           pady=6)
decade_lbl.grid(row=7, column=0, columnspan=1)

total_score_var = tkinter.StringVar(root)
total_score_var .set("Total Score: 0")
total_score_lbl = tkinter.Label(root, textvariable=total_score_var, fg="blue")
total_score_lbl.config(font=('Verdana', '20'))
total_score_lbl.grid(row=7, column=1, columnspan=1)
root.mainloop()
