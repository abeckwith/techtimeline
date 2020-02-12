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
root.configure(background='#B0E0E6')
# encrypted:
PROBLEMS = { 
    "Amazon"        :-994747177,
    "Angry Birds"   :-994636612,
    "Asteroids"     :-994857742,
    "browser"       :-994776661,
    "calculator"    :-994946194,
    "comp w/sound"  :-994813516,
    "CPUs"          :-994916710,
    "desktop"       :-994894597,
    "dumb cellphone":-994901968,
    "email"         :-994916710,
    "Facebook"      :-994673467,
    "Fortnite"      :-994577644,
    "Google"        :-994717693,
    "graphing calc.":-994813516,
    "GUI"           :-994901968,
    "handheld games":-994857742,
    "keyboard"      :-994887226,
    "laptop"        :-994843000,
    "LCD monitors"  :-994739806,
    "Legend of Zelda":-994806145,
    "Mac"           :-994879855,
    "Mario Bros."   :-994828258,
    "Minecraft"     :-994636612,
    "monitor"       :-994901968,
    "mouse"         :-994924081,
    "music player"  :-994725064,    
    "network"       :-994931452,
    "PacMan"        :-994850371,
    "Play Station"  :-994747177,
    "Pong"          :-994909339,
    "programmable"  :-995115727,
    "RAM"           :-994938823,
    "sci. calculator":-994909339,
    "smart phone"   :-994651354,
    "text adv."     :-994879855,
    "touch screen"  :-994828258,
    "transistor"    :-995042017,
    "Tetris"        :-994820887,
    "USB"           :-994732435,
    "video game":-994983049,
    "word proc."    :-994857742,
    "World of Warcraft":-994673467
    }
#DEBUG:
#PROBLEMS = {"39. PacMan"       :-994850371,     "37. Fortnite"     :-994577644}

# get list of inventions/keys:
inventions = list(PROBLEMS.keys()) 
# corresponding list of years:
years_ct      = list(PROBLEMS.values()) 

# make a dictionary of booleans for got_right:
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
    
    
def show_years(decade_ind):
    
    '''go through each display string and add year after each innovation'''
    
    ###### CURRENTLY UNUSED, BUT MAY RE-INSTATE AT SOME POINT ####
    start = 0
    end = 0
    while end != -1:
        end = results_list[decade_ind].find("\n", start)  # results list is the string for the display
        if end != -1:
            year = PROBLEMS[results_list[decade_ind][start:end]]
        
            display = results_list[decade_ind][start:end] + " " + str(year) + "!\n"
            start = end + 1
    results_displays[decade_ind].configure(state="normal") # allow editing of text
    results_displays[decade_ind].delete(1.0, tkinter.END)
    results_displays[decade_ind].insert(tkinter.END, display) # show results in text area
    results_displays[decade_ind].configure(state="disabled") # prevent editing of text#


def setup_menus(c):
    
    '''initial setup of all pulldown menus/also resetting menus when item removed'''
    
    global option_menus, OPTIONS, menu_vars, results_displays, results_list
    global inventions
    # create the optionmenu (pulldown menu) with the options above:
    if c != None:
        for o in option_menus:
            o.grid_forget()
    
    option_menus = []
    menu_vars    = []
    
    OPTIONS = ["SELECT:"] + inventions
    if c != None:
        OPTIONS2 = []

        # THIS WORKS!
        for o in OPTIONS:
            if o != c:
                OPTIONS2.append(o)
        OPTIONS = OPTIONS2    
    # NOTE - COULDN'T SOLVE the problem of set_display(i) sending menu item, not index
    #  so had to forgo a loop here
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[0], 
                                     *OPTIONS,  command = lambda x: set_display(0))
    option_menu.configure(bg="#B0E0E6")
    option_menus.append(option_menu)
    
    #1
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[1], 
                                     *OPTIONS, command = lambda x: set_display(1))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    
    #2
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[2], 
                                     *OPTIONS, command = lambda x: set_display(2))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    #3
    
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[3], 
                                     *OPTIONS, command = lambda x: set_display(3))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    #4
    
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[4], 
                                     *OPTIONS, command = lambda x: set_display(4))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    #5
    
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[5], 
                                     *OPTIONS, command = lambda x: set_display(5))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    #6
    
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[6], 
                                     *OPTIONS, command = lambda x: set_display(6))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    
    #7
    
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    menu_vars.append(menu_var)
    
    option_menu = tkinter.OptionMenu(root, menu_vars[7], 
                                     *OPTIONS, command = lambda x: set_display(7))
    option_menus.append(option_menu)
    option_menu.configure(bg="#B0E0E6")
    

    # place all labels and menus in root window:
    for i in range(num_decades):
        decade_str = str(start_decade + i * 10) + "'s"
        if i < 4:  # first row
            tkinter.Label(root, text=decade_str,  bg="#B0E0E6",
                          font=("Helvetica", "18", "bold")).grid(row=1, column=i, columnspan=1)
            option_menus[i].grid(    row=2, column=i, columnspan=1)
            results_displays[i].grid(row=3, column=i, columnspan=1)
        else:      # second row
            tkinter.Label(root, text=decade_str,  bg="#B0E0E6",
                          font=("Helvetica", "18", "bold")).grid(row=4, column=i % 4, columnspan=1)        
            option_menus[i].grid(    row=5, column=i % 4, columnspan=1)
            results_displays[i].grid(row=6, column=i % 4, columnspan=1)


def check_answers():

    '''called when the check_answers button is clicked - check all answers and update things'''

    global player_score, t, correct_decade, user_decade_counts, decade_counts
    global option_menus, OPTIONS, menu_vars, inventions
    
    player_score -= 50   # lose 50 for every time check answers
    total_score_var.set("Total Score: " + str(player_score))   
    
    ##########################################
    # GO THROUGH ALL DECADE TO FIND MATCHES  #
    ##########################################
    for i in range(num_decades):
        # go through each choice in the list and see if year matches:
        for c in choices[i]:
            val  = str(PROBLEMS[c])                # the year
            srch = str(start_decade + 10 * i)[:3]  # first 3 digits of year
            if val.find(srch) != -1 and not got_right[c]:               # found, so correct decade
                correct_decade += 1
                player_score += 100
                got_right[c] = True
                decade_index = int(srch) - 194
                user_decade_counts[decade_index] += 1
                
                start = results_list[decade_index].find(c)
                end = results_list[decade_index].find("\n", start)  # results list is the string for the display
            
                # change display to show correct answer in caps:
                display = "• " + results_list[decade_index][start:end].upper() + " YES! " + str(val)
                display = results_list[decade_index][0: start] + display + results_list[decade_index][end:]
                results_list[decade_index] = display
                results_displays[decade_index].configure(state="normal") # allow editing of text
                results_displays[decade_index].delete(1.0, tkinter.END)
                results_displays[decade_index].insert(tkinter.END, display) # show results in text area
                results_displays[decade_index].configure(state="disabled") # prevent editing of text#                

                setup_menus(c)        # reset menus without recent correct answers
                inventions.remove(c)  # also remove from list of inventions
                
                break  # no need for the rest of the loop
            else:
                continue
            break          


    # display score and correct count
    old_score = int(score_var.get()[8:]) + 1  # removes "ROUNDS: "
    score_var.set("ROUNDS: " + str(old_score))
    
    decade_var.set("CORRECT DECADE: " + str(correct_decade)  + " of " + str(len(PROBLEMS)))

    # WIN: stop timer
    if correct_decade == len(PROBLEMS):
        root.after_cancel(t)
    

def timer():

    '''show time elapsed'''

    global time, player_score, t
    
    # up by 1 each second, but only subtract from score every 2 seconds
    time += 1         
    if time % 2 == 0:
        player_score -= 1
    
    total_score_var.set("Total Score: " + str(player_score))
    
    
    mins = time // 60
    secs = time % 60
    
    # adjust for 1-digit seconds, then display current time:
    if secs < 10:
        secs = "0" + str(secs)
        
    time_var.set("TIME: " + str(mins) + ":" + str(secs))
    
    t = root.after(1000, timer)  # 1000ms = 1 second


def set_display(i):

    '''menu item selected so add/subtract item from appropriate displays/lists'''

    global started, player_score
    
    if not started:   # first time menu item selected
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
                        height=14,
                        #relief = "ridge",
                        bd = 0, 
                        width=26, bg="#B0E0E6",
                        font=my_font,
                        foreground='white',
                        background='black')
    results_display.configure(state="disabled")
    results_display.config(wrap=tkinter.WORD)
    results_displays.append(results_display)
    results_list.append("")
    
    choices.append([]) # 2D list of what user has chosen for each decade

#  BUTTONS
check_answers_button = tkinter.Button(text = "CHECK ANS", command = check_answers, 
                               padx=10, pady=3, fg="green")
quit_button = tkinter.Button(root, text="Quit", command=quitting_time, padx=10, pady=3)

# lists of zeroes for counts:
decade_counts      = [0] * num_decades
user_decade_counts = [0] * num_decades


for key, value in PROBLEMS.items():
    pt = round(((value - 2623400) / 567 + 1784953) / 13)
    PROBLEMS[key] = pt
    three_dig = pt // 10 - 194
    decade_counts[three_dig] += 1  # first 3 digits of year - 194(0)

# place buttons:
check_answers_button.grid(row=7, column=0, columnspan=2)
quit_button.grid(  row=7, column=3, columnspan=1, pady=20)
check_answers_button.config(font=('Verdana', '30'), borderwidth=5, relief=tkinter.RAISED)
quit_button.config(font=('Verdana', '20'))

#############################################
# make and place all labels for GUI info:
#############################################

score_var = tkinter.StringVar(root)
score_var.set("ROUNDS: 0")
score_lbl = tkinter.Label(root, textvariable=score_var, fg="blue", bg="#B0E0E6")
score_lbl.config(font=('Verdana', '20'))
score_lbl.grid(row=0, column=1, columnspan=1)

time_var = tkinter.StringVar(root)
time_var.set("TIME: 0:00")
time_lbl = tkinter.Label(root, textvariable=time_var, fg="red", bg="#B0E0E6")
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
decade_lbl.grid(row=0, column=2, columnspan=1)

total_score_var = tkinter.StringVar(root)
total_score_var .set("Total Score: 0")
total_score_lbl = tkinter.Label(root, textvariable=total_score_var, 
                                fg="blue", bg="#B0E0E6")
total_score_lbl.config(font=('Verdana', '20'))
total_score_lbl.grid(row=0, column=3, columnspan=1)


setup_menus(None)

root.mainloop()