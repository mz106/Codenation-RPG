import random
import time
import sys
import os


# ********************** ARTWORK FUNCTIONS *******************

# **********************UNICORN/DRAGON ART & TYPEWRITER SPEED***********************
def typewriter_art(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        # time.sleep(0.01)
        time.sleep(0.01)
def print_unicorn():
   typewriter_art(""" \u001b[0m


              ,,))))))));,
           __)))))))))))))),
\|/       -\(((((''''((((((((.
-*-==//////((''  .     `)))))),
/|\      ))| o    ;-.    '(((((                                  ,(,
         ( `|    /  )    ;))))'                               ,_))^;(~
            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
            o_);   ;    )))(((` ~---~  `::           \      %%~~)(v;(`('~
                  ;    ''''````         `:       `:::|\,__,%%    );`'; ~
                 |   _                )     /      `:|`----'     `-'
           ______/\/~    |                 /        /
         /~;;.____/;;'  /          ___--,-(   `;;;/
        / //  _;______;'------~~~~~    /;;/\    /
       //  | |                        / ;   \;;,)
      (<_  | ;                      /',/-----'  _>
       \_| ||_                     //~;~~~~~~~~~
           `\_|                   (,~~ 
                                   \~)
                                    ~~


""")
def print_dragon():
    typewriter_art("""\u001b[32m



                    -,,,__
                     \    ``~~--,,__                /   /
                     /              ``~~--,,_     //--//
          _,,,,-----,\              ,,,,---- >   (c  c))
      ,;''            `\,,,,----''''   ,,-'''---/   /_ ;___        -,_
     ( ''---,;====;,----/             (-,,_____/  /'/ `;   '''''----\ `:.
     (                 '               `      (oo)/   ;~~~~~~~~~~~~~/--~
      `;_           ;    \            ;   \   `  ' ,,'
         ```-----...|     )___________|    )-----'''
                     \   /             \   \\
                     /  /,              `\   \\
                   ,'---\ \              ,---`,;,
                         ```                                  
\u001b[0m
""")
    
# *********************CREDITS FUNCTION & TYPEWRITER SPEED*****************
def typewriter_credits(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        # time.sleep(0.05)
        time.sleep(0.01)


def print_credits():
    typewriter_credits(""" 

\u001b[33m
   ____ ____  _____ ____ ___ _____ ____  
  / ___|  _ \| ____|  _ \_ _|_   _/ ___| 
 | |   | |_) |  _| | | | | |  | | \___ \ 
 | |___|  _ <| |___| |_| | |  | |  ___) |
  \____|_| \_\_____|____/___| |_| |____/ 
                                          \u001b[0m 
   _____________________________________
 / \                                     \.
|   |                                    |.
 \_ |\u001b[33m         Michael Zwierzanski\u001b[0m        |.
    |      Lead Dev / Project Manager    |.
    |                                    |.
    |\u001b[33m          Maebh Ní Ghuairim\u001b[0m         |.
    |          Chief Storyteller/        |.
    |          Righter of Wrongs         |.
    |                                    |.
    |\u001b[33m            Luke Beech\u001b[0m              |.
    |           Trello Master/           |.
    |          Art Connoisseur           |.
    |                                    |.
    |\u001b[33m            Ryan Heenan\u001b[0m             |.
    |            Admin Guru/             |.
    |          Art Connoisseur           |.
    |   _________________________________|____
    |  /                                     /.
    \_/_____________________________________/.
    
 


     
            $$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$
            $$$'`$$$$$$$$$$$$$'`$$$$$
            $$$$  $$$$$$$$$$$  $$$$$$
            $$$$. `$' \' \$`  $$$$$$$
            $$$$$. !\  i  i .$$$$$$$$
            $$$$$$   `--`--.$$$$$$$$$
            $$$$$$L        `$$$$$^^$$
            $$$$$$$.   .'   ""~   $$$
            $$$$$$$$.  ;      .e$$$$$
            $$$$$$$$$   `.$$$$$$$$$$$
            $$$$$$$$    .$$$$$$$$$$$$
            $$$$$$$     $$$$$$$$$$$$$
            -------------------------
\u001b[35m             With Special Thanks To\u001b[0m
            -------------------------
                     Chantela
                       Dave
                       Leon
                       Will
                       Tim
                       ...

           and to Danny for "de Embalmer

       Powered by brains, magic and caffeine

\u001b[33m

 ______                                           
/\__  _\                                          
\/_/\ \/    __     __      ___ ___                
   \ \ \  /'__`\ /'__`\  /' __` __`\              
    \ \ \/\  __//\ \L\.\_/\ \/\ \/\ \             
     \ \_\ \____\ \__/.\_\ \_\ \_\ \_\            
 __   \/_/\/____/\/__/\/_/\/_/\/_/\/_/            
/\ \  /\ \    /\_ \  /\_ \                        
\ `\`\\/'/  __\//\ \ \//\ \     ___   __  __  __  
 `\ `\ /' /'__`\\ \ \  \ \ \   / __`\/\ \/\ \/\ \ 
   `\ \ \/\  __/ \_\ \_ \_\ \_/\ \L\ \ \ \_/ \_/ )
     \ \_\ \____\/\____\/\____\ \____/\ \___x___/'
      \/_/\/____/\/____/\/____/\/___/  \/__//__/ 


\u001b[0m

    
\u001b[35m                                                     ;                                                
\u001b[31m                                       :            ED.                                              
\u001b[32m                         .,           t#,           E#Wi                       ,;                    
\u001b[33m                        ,Wt          ;##W.          E###G.                   f#i                     
\u001b[34m                       i#D.         :#L:WE          E#fD#W;                .E#t                      
\u001b[35m                      f#f          .KG  ,#D         E#t t##L              i#W,                       
\u001b[36m                    .D#i           EE    ;#f        E#t  .E#K,           L#D.                        
\u001b[37m                   :KW,           f#.     t#i       E#t    j##f        :K#Wfff;                      
\u001b[35m                   t#f            :#G     GK        E#t    :E#K:       i##WLLLLt                     
\u001b[31m                    ;#G            ;#L   LW.        E#t   t##L          .E#L                         
\u001b[32m                     :KE.           t#f f#:         E#t .D#W;             :#E:                       
\u001b[33m  L.                  .DW:           f#D#;          E#tiW#G.             t#,WW;        L.            
\u001b[34m  EW:        ,ft        L#,           G#t           E#K##i t            ;##W.D#;       EW:        ,ft
\u001b[35m  E##;       t#E         jt       ..   t   GEEEEEEELE##D.  Ej          :#L:WE tt       E##;       t#E
\u001b[36m  E###t      t#E                 ;W,       ,;;L#K;;.E#t    E#,        .KG  ,#D         E###t      t#E
\u001b[37m  E#fE#f     t#E                j##,          t#E   L:     E#t        EE    ;#f        E#fE#f     t#E
\u001b[35m E#t D#G    t#E               G###,          t#E          E#t       f#.     t#i       E#t D#G    t#E
\u001b[31m  E#t  f#E.  t#E             :E####,          t#E          E#t       :#G     GK        E#t  f#E.  t#E
\u001b[32m  E#t   t#K: t#E            ;W#DG##,          t#E          E#t        ;#L   LW.        E#t   t#K: t#E
\u001b[33m  E#t    ;#W,t#E           j###DW##,          t#E          E#t         t#f f#:         E#t    ;#W,t#E
\u001b[34m  E#t     :K#D#E          G##i,,G##,          t#E          E#t          f#D#;          E#t     :K#D#E
\u001b[35m  E#t      .E##E        :K#K:   L##,          t#E          E#t           G#t           E#t      .E##E
\u001b[36m  ..         G#E       ;##D.    L##,           fE          E#t            t            ..         G#E
\u001b[37m              fE       ,,,      .,,             :          ,;.                                     fE
\u001b[35m               ,                                                                                    ,




""")
    

def typewriter(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        # time.sleep(0.005)
        time.sleep(0.005)
typewriter("""\u001b[32m
  _____ _                               
 |_   _| |__   ___                      
   | | | '_ \ / _ \                     
   | | | | | |  __/                     
  _|_|_|_| |_|\___|             _       
 |_   _| __ __ _  __ _  ___  __| |_   _ 
   | || '__/ _` |/ _` |/ _ \/ _` | | | |
   | || |_| (_| | (_| |  __/ (_| | |_| |
   |_||_/ _\__,_|\__, |\___|\__,_|\__, |
  / _ \| |_      |___/            |___/ 
 | (_) |  _|                            
  \___/|_|                              
                                        
  __  __       ____                      _     _           
 |  \/  | ___ / ___|_ __ _   _ _ __ ___ | |__ | | ___  ___ 
 | |\/| |/ __| |  _| '__| | | | '_ ` _ \| '_ \| |/ _ \/ __|
 | |  | | (__| |_| | |  | |_| | | | | | | |_) | |  __/\__ )
 |_|  |_|\___|\____|_|   \__,_|_| |_| |_|_.__/|_|\___||___/
                                                           
------------------------------------------------------------
\u001b[37m
....................................................................................................
....................,,,,...........................................;?S#@@#S+,.......................
...............;S@?@S#@@@@S,...................................,?@@@;,;@@@S%@S,.....................
............:%S@@*,.;@@%:,:@?................................;@%+@@@?:?%@#@@+%@,....................
..........;@@S,*%#SS@@@@@@##@;.............................:@@@@S;*@@@@@S@S%@@@*....................
........,S@@S?+;;?@@@@S:,%@@@S............................:#*:......?@@@S..:%@@@;...................
.........,........+@@@?*,S@@@@S.....................................+@@@@@?@@@@@@:..................
..................%@@@@@@@#@@@@?...................................:@@@@@@@@*?*S@#,.................
.................*@@@@@@@#;.;@@@:..................................%@@@@@@@?:.:S@@+.................
.................%@@@@@@@@S+#S@@?..................................%#?@@@@@@##@@@@S.................
.................%S:#@#@@@@@@@@@@,.................................S@+,;S@@@@@@?S@@;................
................,#@@S#@@@@@@@,#@@*................................;@@@@@@@@@@@@:+@@%................
................%@@@@@@@@*@@#S;*@#,..............................,#@@@@@@#%:;*#@@@@@:...............
...............+@@@@@@@S;..%@@@@@@+..............................%@#@@@@@@S,:%@@@@@@%...............
..............;@@*?%S@@@SS@S@@@@@@#......................,:+*?%:%@S;.:@@@@@@@@@@@%@@@;,.............
.....:?#@@@@;.*@?:.:#@@@@@@@@++:@@@*SS%?+:...........,?@@@@@@S..:@@%*SS@@@@@@@@?.,+#S.;@@@@@S*,.....
..,%@@@@@@@S...?@#@@@@@@@@@@#;::S#:..S@@@@@@#*......*@@@@@@@@@,..,%@@@@@@@@@@@@@#?@;...S@@@@@@@@%,..
.,#@@@@@@@@@+...,%@@@@@@@@@@@@@S:...:@@@@@@@@@@*...,@@@@@@@@@@#,....;%@@@@@@@@@#*,...,S@@@@@@@@@@S..
.,#@@@@@@@@@@?......,;*%%%%*;,.....+*+++?%#@@@@*....?@@@@@@@@@@@%:..................;*%##@#S%***+,..
..:#@@@@@@@@@@@@?:..............+S@@@@@@@@@@#?,......;#@@@@@@@@@@@@@S*:,...,,;;,:S@@@@@@@@@@S*,.....
....:%@@@@@@@@@@@@@@@##S##S*;?@@@@@@@@#%+:..............;%@@@@@@@@@@@@@@@@#*+?@@@@@@#%+:,...........
........:+%#@@@@@@@@@#%**S@@@#%*;:............................,:;+*???%%S@@S?+:,....................
.................,:;;+;:,...........................................................................
....................................................................................................
....................................................................................................

\u001b[33m  
  _     _       _     _  ___                                        ____             _    ___ 
 | |   (_) __ _| |__ | ||__ \               ___  _ __              |  _ \  __ _ _ __| | _|__ )
 | |   | |/ _` | '_ \| __|/ /              / _ \| '__|             | | | |/ _` | '__| |/ / / /
 | |___| | (_| | | | | |_|_|              | (_) | |                | |_| | (_| | |  |   < |_| 
 |_____|_|\__, |_| |_|\__(_)               \___/|_|                |____/ \__,_|_|  |_|\_\(_) 
          |___/                                                                                   
\u001b[0m
""")

# 


# ******************************* ARTWORK FUNCTIONS*****************************




name_input_capitalize = " "
color_input_lower = " "
# wizard_roll_choice is for the die roll choice if user succeeds in answering the riddle
wizard_roll_choice = 0



# intro - backstory/text to be edited and improved
# intro function is to be called to initiate the game. Intro function MUST be placed at the bottom of the code

# class Wizard:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def wizard_attack(self):
#         if self.color == "light":
#             return random.randint(1,12)
#         elif self.color == "dark":
#             return random.randint(1,12)

# new_wizard = Wizard(name_input_capitalize, color_input_lower)   
# # new_wizard = Wizard("Michael", "light")

# ***************************************************************************************

#==========Test function - ignore unless testing griffin function/wizard class ====================
# def end_test_function():
#     print("is test ok?")
#     print(new_wizard)
#     print(new_wizard.name)
#     print(new_wizard.color)
#=============================
#======= To be given story and implemented later ======================
# def fight_the_griffin():
#     griffin_attack_num = random.randint(0,10)
#     wizard_attack_num = new_wizard.wizard_attack()
#     if griffin_attack_num > wizard_attack_num:
#         print("griffin number " + str(griffin_attack_num))
#         print("wizard numbner " + str(wizard_attack_num))
#         print("The griffin wins!")
#     elif wizard_attack_num > griffin_attack_num:
#         print("griffin number " + str(griffin_attack_num))
#         print("wizard numbner " + str(wizard_attack_num))
#         print("The Wizard wins")    
#     # end_test_function()
# ==================


# =========== to delete - for testing purposes
# def light_path_random_choice_two():
#     print("one step further")

#=============================================================================================================

#=============================================== End credits function for both light and dark ================================================+

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Yet to complete !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

# def temp_end_credits_placeholder():
#     print("I'm here as a temp function for the ending credits")
#=============================================================================================================================================

#================================================ Temp end function dark path ====================================================================

# def temp_dark_end_function():
#     print("This is a temp end for the dark path for testing")
#===================================================================================================================================
#===============================================Dark Ending Final Function ========================================================

def dark_final_battle_loss_return_input():
    final_battle_loss_input = input("    Please enter return or stay: ")
    final_battle_loss_input_lower = final_battle_loss_input.lower()
    
    if final_battle_loss_input_lower == "return":
        typewriter("    You have chosen to return to the fray...")
        count = 5
        while count > 0:
            print("    " + str(count))
            count = count - 1
        dark_ending_riddle_intro()
            
    elif final_battle_loss_input_lower == "stay": 
        print("    Enjoy your final embrace with nothingness...")
        time.sleep(5)
        print_credits()
        sys.exit()
        #!!!!!!!!!!!!!!!!!!!!!!!! edit the above function when complete !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

    else:
        time.sleep(2)
        dark_final_battle_loss_return_input()
# #======================================================================================================
# #====================================================================Dark ending final showdown function ======================================================

def dark_ending_final_showdown(par1, par2):
    #In this function, par1 refers to the users die roll, and par 2 to the Nekroids
    typewriter("""
    McGrumbles rolling...""")
    print("")
    time.sleep(1)
    count = 5
    while count > 0:
        print("    " + str(count))
        count = count - 1
        time.sleep(0.5)
    
    typewriter("    McGrumbles rolls " + str(par2))
    
    print("")
    
    print("""
    You roll...""")
    print("")
    time.sleep(1)
    count = 5
    while count > 0:
        print("    " + str(count))
        count = count - 1
        time.sleep(0.5)
    
    typewriter("    You have rolled " + str(par1)) 
    
    # here, change wizard roll to object method wizard_attack() if michael can get working

    if par2 > par1: 
        typewriter("""
        You have failed! The McGrumbles has bested you! You feel the his magic embrace you with the cold touch of death! Farewell to thee, wizard of 
        little acclaim...""")
    
        typewriter("""
        You may return to the final challenge and battle McGrumbles beast once more. Do you wish to go return to the fray, or stay in the underworld 
        to embrace your demise?""")
        time.sleep(2)

        dark_final_battle_loss_return_input()
    
    elif par1 > par2:
        typewriter("""
        You have defeated McGrumbles! He utters his final words...""")
        typewriter("""
        'You know not the power of the dragon...use it wisely...'""")
        typewriter("")
        typewriter("""
        With his last breath gone, you step over the crumpled body of McGrumbles, the wizard that helped you towards your destiny, and walk towards 
        the dragon. The ultimate power is finally yours...""")

        typewriter("")

        print_dragon()
        print_credits()
        sys.exit()

    elif par1 == par2:
        typewriter("""
        A draw! This round you matched McGrumbles. But you must roll better next time!""")
        typewriter("")
        time.sleep(2)
        dark_ending_die_roll(wizard_roll_choice)    
    else: 
        typewriter("error - check code now!!!!!!1")
        #for testing
    
#===================================================================== Dark end die roll function =======================================================
def dark_ending_die_roll(par):
    #line 117 for testing - replace with 118
    # mc_grumbles_roll = 1
    mc_grumbles_roll = random.randint(1,12)
    dark_ending_final_showdown(wizard_roll_choice, mc_grumbles_roll)
    # if par == 0:
    #     par = random.randint(1,12)
    #     light_ending_final_showdown(wizard_roll_choice, nekroid_roll)

    # elif par > 0:
    #     light_ending_final_showdown(wizard_roll_choice, nekroid_roll)


def dark_ending_riddle():
    count = 3
    while count > 0:
        print("")
        riddle_answer = input("    Enter your answer to the riddle...and pray! ") 
        riddle_answer_lower = riddle_answer.lower()
        if riddle_answer_lower == "wand":
            time.sleep(3)

            typewriter("""
            Success! You have cast the spell and can now manipulate reality!""") 
            print("")
            while True:
                try:
                    global wizard_roll_choice
                    wizard_roll_choice = int(input("   Enter your desired die-roll: "))
                    print("")
                except ValueError:
                    print("")
                    print("    Please enter numerals, not letters! ")
                    print("")
                    time.sleep(2)
                    continue
                else:
                    dark_ending_die_roll(wizard_roll_choice)
                    break
            count = 0
            
        # else:
        #     time.sleep(3)

        #     print("""
        #     You have failed, meager spellcaster! You must rely on Lady Luck...""")
        #     wizard_roll_choice = random.randint(1,6)
        #     dark_ending_die_roll(wizard_roll_choice)
        elif riddle_answer_lower != "wand" and count == 3:
            typewriter("""
            First atempt, you failed! You have two more atempts to answer the riddle... """)
            time.sleep(3)
            count = count - 1

        elif riddle_answer_lower != "wand" and count == 2:
            typewriter("""
            Second atempt, you failed! You have one more try.""")

            print("")

            time.sleep(3)

            typewriter("""
            Here's a hint - try looking at the capital letters...""")
            count = count - 1

        elif riddle_answer_lower != "wand" and count == 1:
            typewriter("""
            You have failed, meager spellcaster! You must rely on Lady Luck...""")
            count = 0
            wizard_roll_choice = random.randint(1,6)
            # dark_ending_die_roll(wizard_roll_choice)
            
            # test_function(wizard_roll_choice)
            # break
    dark_ending_die_roll(wizard_roll_choice)
         

#===================================================================Dark end function riddle =======================================================

def dark_ending_riddle_intro():
    
    typewriter("""
    ...but before you cast your fate you look into your spell book, rushing to find the correct spell as McGrumbles prepares his D12 attack. With only 
    a D6, you hope that you can find a spell...""")
    
    typewriter("""
    ...finding the right page, you realise that the incantation is in the form of a riddle... If you can cast the spell, you can choose your die roll! If not, 
    pray the Goddess of Chance smiles upon your soul this day...""")

    print("")

    typewriter("""
    The riddle reads;
        'if Witches Aim Needlessly Down, you'll need this to protect you...""")

    print("")

    dark_ending_riddle()


#=========================================================================================================
   

# #=========================================== Dark ending story function =================================================================
def dark_end_story():
    typewriter("""
    ...finally! After so much searching, you have reached the fabled Arnok, land of the dragon! You easily find the lair of the dragon, and go to claim 
    your prize, only,... you thought that you had killed McGrumbles, but here he is, standing at the lair entrance, seemingly with the dragon under his 
    control...""")

    print("")

    typewriter("""
    'You thought that you could end my life so easily! Ha! Your powers have not yet even begun to mature, nevermind be able to rival mine!'""")

    print("")

    typewriter("""
    McGrumbles raises a clenched fist into the air, holding a D12 die. 'Remember', he says, 'I can take Double anything you could!' (Withnail and I ref)""")

    print("")

    typewriter("""
    Confused by this out of context reference, you point your wand and cast a spell of creation, confident that you can create a die to vanquish that 
    of McGrumbles! But oh know! It is only a D6 - indeed McGrumbles have double that he spoke promised!""")
    # the random number if you cannot pass the riddle is between 1 to 6, 1 to 12 for Mc Grubmbles
    print("")

    print("")

    typewriter("""
    'Prepare to die!' shouts McGrumbles""")

    print("")

    typewriter("""
    You look up and see the dragon's tail. Inspired by the sight of your destiny, you steel you self and prepare to roll.....""")

    time.sleep(3)
    dark_ending_riddle_intro()

#=============================================== Dark path sequence two ===================================================================
#============== repeated inside function, kept for illustration
# para_three = """
# A light wizard has been spotted in your village. As your natural enemy, 
# you desire to end his pathetic life.
# Do you:

# A: Enchant the wizard. Under your spell you can force them to do anything you desire.
    
# or
    
# B: Poison the town well.
# """

para_four = """
    Hearing the pain of the dying villagers, McGrumbles comes their aid, and
    with the body count rising, the remaining villagers begin to suspect foul play. 
    Do you:

    A: Accuse McGrumbles. As the only other wizard, you can surely pass the blame onto him.
    
    or
    
    B: Summon a soul dragon to feast on the corpses and finish off the weak villagers."""
    
def dark_path_quest_two():
    typewriter(para_four)
    my_input = input("    Choose A or B: ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        Your attempt to pass the blame onto the well respected 
        and wise Mcgrumbles fails. You suffer his wrath as he casts a 
        spell and engulfs you in flame. How foolish.""")
        time.sleep(3)
        typewriter("...but death does not take you today! You use your dark powers to to move backwards in time, to when you entered the village...")
        time.sleep(3)

        dark_path_two() 
    elif my_input_lower == "b":  
        typewriter("""
        You conjour a soul dragon, which lives only long enough to take the sould or the nearly dead. 
        With the village conquered, you step over the dead McGrumbles, his body beaten to a pulp 
        by the enraged villagers, laying in the Garden of Betryal, waiting for 'de Embalmer'. You 
        smirk wryly at him, hoping to continue to satisfy your bloodlust on the way to the land of Arnok, 
        to take your dragon...""")  

        dark_end_story()
    else:
        typewriter("    please type A or B")
        time.sleep(2)
        dark_path_quest_two()

def dark_path_two():
    typewriter("""
    You materialize in the distant village of Vanitair. A light wizard has been spotted milling
    around, waiting for an unsuspecting dark wizard. As your natural enemy, you desire to end 
    his pathetic life...
    Do you:

    A: Enchant the wizard. Under your spell you can force them to do anything you desire.
    
    or
    
    B: Poison the town well.""")
    print("")
    time.sleep(2)
    my_input = input("    Choose A or B: ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
    With the wizard under your spell, you lead him to the graveyard, 
    excited at the chance to bury the wizard alive. 
    A shadowy figure emerges and plunges a dagger into your heart. 
    The light wizard tricked you. They were never under your spell...""")
        time.sleep(3)
        typewriter("""
    ...but death does not take you today! You use your dark powers to to move 
    backwards in time, to when you entered the village.""")
        time.sleep(3)
        dark_path_two() 
    elif my_input_lower == "b":
        time.sleep(2)
        dark_path_quest_two()
    else:
        typewriter("    please type A or B")
        time.sleep(2)
        dark_path_two()

#==========================================================================================================================================

#================================================= Daark path sequence one ====================================================================

para_one = """
    You find yourself standing in the far-flung village of Tolstung. Among the villagers you identify 
    a messenger carrying a list containing known dark wizards. This list will be handed to the Empire 
    in order to purge your dreaded kind from this world.

    Your name is on this list...

    Do you:

    A: Let the messenger pass by.
    An unexpected death of a messenger would surely alert the imperial troops.
    
    or
    
    B: Intercept the messenger."""

para_two = """
    The empire is on high alert since the expected messenger failed to show. 
    Imperial troops have been sent to patrol in your vicinity. 

    Do you: 

    A: Let the troops pass by. If you do, you'll need to find a more permanent way of avoiding execution. 

    B: Confront the troops"""
def dark_path_quest_one():
    typewriter(para_two)
    my_input = input("    Choose A or B: ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        Sneaking away from the Empire's patrol, you summon McGrumbles. As he greets you,
        you take your wand and slay him! Stealing his identity, you now have the perfect
        cover to continue with your nefarious deeds...""") 

        dark_end_story()
    elif my_input_lower == "b":  
        typewriter("""
        A stupid move, you are not powerful enough to take on a garrison. They easily overwhelm you. 
        As your life slowly fades from you, you gaze at the stars and contemplate your foolish decisions...""")
        ("...but you are not done yet! You use your dark powers to move backwards in time, to when you entered the village.")
        time.sleep(5)
        dark_path_one()  
    else:
        typewriter("    please type A or B")
        time.sleep(2)
        dark_path_quest_one()

def dark_path_one():
    typewriter(para_one)
    time.sleep(2)
    my_input = input("    Choose A or B: ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        The Empire now have the list. Aware of your location, soldiers ambush you. Now captured,  execution soon awaits...""")
        time.sleep(3)
        print("")
        typewriter("""
        ...but not for you! You use your dark powers to move backwards in time, to when you entered the village.""")
        time.sleep(3)
        dark_path_one() 
    elif my_input_lower == "b":
        time.sleep(2)
        typewriter("""
        You cast a spell, confusing the messenger while you calmly approach 
        and behead the poor soul using your sword. Now in possession of the list, 
        you toss it into a fire. You are now free from the empire, ready to 
        continue your quest...""")
        time.sleep(2)
        dark_path_quest_one()
    else:
        typewriter("    please type A or B")
        time.sleep(2)
        dark_path_one()

#=============================================================================================================================================

#=============================================== Dark path random choice/paths ===============================================================


def dark_path_random_choice():

    typewriter("""
    In the beginning, you chose the dark path because it was a magical path that focused on power, allowing you to 
    chase your destiny... or so you thought. You have always known that finding the black dragon of Arnok, a 
    mystical creature famed for the power to destroy even adamantium, has been your life's purpose.""")
    
    print(" ")

    typewriter("""
    But those dark wizards! Obsessed with their rules, keeping you from your destiny! And so, you started your search, 
    many leagues from the Kingdom of Escherton, pledging to wander until you found the one that you seek...
    the one that can help you...""")

    print(" ")

    typewriter("""
    ...the one known only as McGrumbles...""" )

    print(" ")

    typewriter("""
    'And so, you have found yourself in the Glade of Ill Portends!' McGrumbles towers above you. 'You are here seeking 
    adventure. Ha Ha! THAT is definately something that I can help you with....'""")

    print(" ")

    print("""
    McGrumbles reaches for his wand and points it directly at you.""")

    print(" ")

    typewriter("""
    'Where you will find yourself, I do not know...'""")

    print(" ")

    typewriter("""
    You find yourself spinning in a vortex the like of which you have not seen before...""")

    print(" ")
    
    time.sleep(2)

    typewriter("""
    Who knows where you will land...""")

    time.sleep(2)
    print(" ")

    vortex_adjective_list = ["    Swirling", "    Stars", "    What's that!"]

    for x in vortex_adjective_list:
        print(x)
        print(" ")
        time.sleep(3)
        
    dark_path_choice_list = [dark_path_one, dark_path_two]
    random.choice(dark_path_choice_list)()    

#=============================================================================================================================================

#=============================================== End functions Light path ====================================================================

#================================================ Temp end function light path ====================================================================



# def temp_light_end_function():
#     print("This is a temp end for the light path for testing")




#===================================================================================================================================
#============
def light_final_battle_loss_return_input():
    final_battle_loss_input = input("    Please enter return or stay: ")
    final_battle_loss_input_lower = final_battle_loss_input.lower()
    
    if final_battle_loss_input_lower == "return":
        typewriter("    You have chosen to return to the fray...")
        count = 5
        while count > 0:
            print("    " + str(count))
            count = count - 1
        light_ending_riddle_intro()
            
    elif final_battle_loss_input_lower == "stay": 
        typewriter("    Enjoy your final embrace with nothingness...")
        time.sleep(5)
        print_credits()
        sys.exit()
        #!!!!!!!!!!!!!!!!!!!!!!!! edit the above function when complete !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

    else:
        
        time.sleep(2)
        light_final_battle_loss_return_input()
# #======================================================================================================================================================
# #====================================================================Light ending final function ======================================================

def light_ending_final_showdown(par1, par2):
    #In this function, par1 refers to the users die roll, and par 2 to the Nekroids
    typewriter("""
    Nekroid rolling...""")
    print("")
    time.sleep(1)
    count = 5
    while count > 0:
        print("    " + str(count))
        count = count - 1
        time.sleep(0.5)
    
    typewriter("    The Nekroid rolls " + str(par2))
    
    print("")
    
    typewriter("""
    You roll...""")
    print("")
    time.sleep(1)
    count = 5
    while count > 0:
        print("    " + str(count))
        count = count - 1
        time.sleep(0.5)
    
    print("    You have rolled " + str(par1)) 
    
    # here, change wizard roll to object method wizard_attack() if michael can get working

    if par2 > par1: 
        typewriter("""
        You have failed! The monster has bested you! You feel the Nekroid's tentecales embrace you with the cold touch of death! Farewell to thee, 
        wizard of little acclaim...""")
    
        typewriter("""
        You may return to the final challenge and battle the nekroid beast once more. Do you wish to go return to the fray, or stay in the underworld 
        to embrace your demise?""")
        time.sleep(2)

        light_final_battle_loss_return_input()
    
    elif par1 > par2:
        typewriter("""
        You have defeated the Nekroid! McGrumbles approaches you from the forest, unicorn in tow...""")
        typewriter("""
        'My fine wizard! You have overcome all challenges that have beset you. You are indeed worthy of belonging to the brethren of wizards! And
        now, the purpose of your quest!'""")
        print("")
        typewriter("""
        You stroke the mane of the unicorn, the silky feeling on your fingers endorsing the feeing of victory, knowing that you have finally
        found the creature that you have searched for for so long...""")

        print("")

        print_unicorn()
        print_credits()
        sys.exit()

    elif par1 == par2:
        typewriter("""
        A draw! This round you matched the monster. But you must roll better next time!""")
        print("")
        time.sleep(2)
        light_ending_die_roll(wizard_roll_choice)    
    else: 
        typewriter("error - check code now!!!!!!1")
        #for testing
    
#===================================================================== Light end die function =======================================================
def light_ending_die_roll(par):
    #line 453 for testing - replace with 454
    # nekroid_roll = 12
    nekroid_roll = random.randint(1,12)
    light_ending_final_showdown(wizard_roll_choice, nekroid_roll)
    #below left for reference
    # if par == 0:
    #     par = random.randint(1,12)
    #     light_ending_final_showdown(wizard_roll_choice, nekroid_roll)

    # elif par > 0:
    #     light_ending_final_showdown(wizard_roll_choice, nekroid_roll)

#===================================================================Light end function riddle =======================================================
def light_ending_riddle():
    count = 3
    while count > 0:
        print("")
        riddle_answer = input("    Enter your answer to the riddle...and pray! ") 
        riddle_answer_lower = riddle_answer.lower()
        if riddle_answer_lower == "newt":
            time.sleep(3)

            typewriter("""
            Success! You have cast the spell and can now manipulate reality!""") 
            print("")
            while True:
                try:
                    global wizard_roll_choice
                    wizard_roll_choice = int(input("   Enter your desired die-roll: "))
                    print("")
                  
                except ValueError:
                    print("")
                    typewriter("    Please enter numerals, not letters! ")
                    print("")
                    time.sleep(2)
                    continue
                else:
                    light_ending_die_roll(wizard_roll_choice)
                    break
            count = 0
            
    
        elif riddle_answer_lower != "newt" and count == 3:
            typewriter("""
            First atempt, you failed! You have two more atempts to answer the riddle... """)
            time.sleep(3)
            count = count - 1

        elif riddle_answer_lower != "newt" and count == 2:
            typewriter("""
            Second atempt, you failed! You have one more try.""")

            print("")

            time.sleep(3)

            typewriter("""
            Here's a hint - try looking at the capital letters...""")
            count = count - 1

        elif riddle_answer_lower != "newt" and count == 1:
            typewriter("""
            You have failed, meager spellcaster! You must rely on Lady Luck...""")
            count = 0
            wizard_roll_choice = random.randint(1,6)
            # dark_ending_die_roll(wizard_roll_choice)
            
            # test_function(wizard_roll_choice)
            # break
    light_ending_die_roll(wizard_roll_choice)        


def light_ending_riddle_intro():
    
    typewriter("""
    ...but before you cast your fate you look into your spell book, rushing to find the correct spell as the Nekroid prepares its D12 attack. Finding the 
    right page, you realise that the incantation is in the form of a riddle... If you can cast the spell, you can choose your die roll! If not, pray the 
    Goddess of Chance smiles upon your soul this day...""")

    print("")

    typewriter("""
    The riddle reads;
        'Now Enter, Wizard True, the first ingredient for your potion blue...""")

    print("")

    time.sleep(1)

    light_ending_riddle()

#=========================================================================================================
   
# #=========================================== Light ending story function =================================================================
def light_end_story():
    typewriter("""
    Celador! Finally, you have reached the land of the unicorn, the land that you have sought for so long! The healing power of the 
    unicorn is within your grasp! Quick, ahead of you, look! In the clearing, the unicorn is grazing majestically. More beautiful than 
    than any wonder that you have seen before, it shines brightly as you start to approach it, gently, slowly, so as not to cause 
    alarm...""")

    print("")

    typewriter("""
    Suddenly, the unicorn raises it's head and, like the crack of a whip, charges off into the forest behind. You make motion to chase, but, 
    out of nowhere, a swirl of black smoke rushes upwards from a newly appearing fissure in the ground. And out of the smoke comes ...""")

    print("")

    typewriter("""
    ...McGrumbles!""")

    print("")

    typewriter("""
    'Sooooooo my dear wizard, you have reached my final challenge! If you have thought that your journey thus far has been fraught with danger, 
    then think again! I will now put before you a peril more deadly than even the dreaded Rancor!'""")

    print("")

    typewriter("""
    Before you appears an example of the most feared creature in all of Escherton - the Nekroid beast! Its stench is overpowering, and you must
    battle to stay conscious.""")

    print("")

    typewriter("""
    'This is the final test of your magic!' McGrumbles hands you what appears to be a small pebble. 'This is a test to see if have harnessed
    the power to manipulate reality!' You look at the pebble in your palm, and notice that it is, in face, a D12 die. 'Unleash the power of the
    die and roll higher than the monster, or you shall surely die!' """)

    print("")

    typewriter("""
    You look up and see the tip of the unicorn's horn. Inspired by the sight of your destiny, you steel yourself and prepare to roll.....""")

    time.sleep(3)
    light_ending_riddle_intro()
#==============
#==============================================================================================================================================


# ===========================Light Path Two Sequence=================================================================================

def Light_Path_Two_Death_Loop():
    my_input = input("    Would you like to begin again? Please type yes or no:  ")
    my_input_lower = my_input.lower()
    if my_input_lower == "yes":
        Light_Path_Two_First_Paragraph()
    elif my_input_lower == "no":
        print_credits()
    else:
        Light_Path_Two_Death_Loop()

def Light_Path_Two_Final_Paragraph():
    typewriter("""
    You get so close you can smell the rotting fish on 
    her breath (at least you hope it is fish). She opens
    up her palms to reveal a perfect pearl. 'I know you're
    here because McGrumbles sent you,' she says softly. 'Let
    him know I miss him. Tell him to come visit me. Tell him 
    I've spared your life just for him.' She puts the pearl 
    into your hands. 'Tell him.'
    """)
    time.sleep(1)
    typewriter("""
    Armed with the pearl, you make your way back to Celador.
    Once you're back, you'll only face one more challenge,
    before you can move on from this wretched affair. You're
    so close... 
    """)

    light_end_story()

def Light_Path_Two_Second_Option_Set_Input_X():
    typewriter("""
    You've insulted the mermaid. You see it instantly in
    her eyes. Before you can react, her tail whips up. It 
    is the last thing you see before you're decapitated.
    """)
    time.sleep(1)
    print("""
    GAME OVER
    """)

    Light_Path_Two_Death_Loop()

def Light_Path_Two_Second_Option_Set_Input_Y():
    typewriter("""
    She studies you for a moment, then nods. 'You're in a hurry', 
    she comments. 'You're lucky I've already eaten today.' A 
    shiver runs down your spine. 'Come closer, I'll show you what 
    you're looking for.'
    """)
    Light_Path_Two_Final_Paragraph()

Light_Path_Two_Random = [Light_Path_Two_Second_Option_Set_Input_X, Light_Path_Two_Second_Option_Set_Input_Y]    

def Light_Path_Two_Second_Option_Set_Input():
    my_input = input("    Please type A or B:   ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        random.choice(Light_Path_Two_Random)()
        # ****this is for testing, revert back to 789
        # Light_Path_Two_Second_Option_Set_Input_Y()

    elif my_input_lower == "b":
        typewriter(""" 
        She smiles at you. 'I like you', she says. 'And you're
        lucky I've already eaten.' A shiver runs down your spine. 
        'Come closer, I'll show you what you're looking for.'
        """)
        Light_Path_Two_Final_Paragraph()

    else: Light_Path_Two_Second_Option_Set_Input()


def Light_Path_Two_Second_Option_Set():
    typewriter("    You have two options:")
    time.sleep(0.5)
    typewriter("""
    A -  You don't want to engage in small talk. The quicker
    you're gone, the safer you are. You ask her if she can 
    help you.
    """)
    time.sleep(0.5)
    typewriter("""
    B - You greet her in return, and add a compliment about her
    beauty. Mermaids like to be complimented, even if they are 
    likely to kill you either way.
     """)
    Light_Path_Two_Second_Option_Set_Input()

def Light_Path_Two_Second_Paragraph():
    typewriter("""
    You arrive to the rock, and are greeted by the most 
    beautiful woman you've ever seen. But you know she is 
    no woman. This is a mermaid and you must be on guard. 
    She flicks her tail behind the rock, as if you hadn't 
    already realised. "Good morning", she says sweetly, but 
    it sounds like a hiss.
    """)
    Light_Path_Two_Second_Option_Set()


def Light_Path_Two_Point_One_Option_Set_Input():
    my_input = input("    Please type A or B:   ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        You take a left and walk down a narrow path.
        The light rapidly disappears, and you begin to 
        forget where you started from. In the pitch 
        darkness, you stumble around, hopelessly trying 
        to get back, but it's an impossible task.
        """)
        typewriter("""
        You die a few days later of dehydration.
        """)
        time.sleep(1)
        typewriter("""
        GAME OVER
        """)

        Light_Path_Two_Death_Loop()

    elif my_input_lower == "b":
        typewriter("""
        Whenever faced with such a choice, you always chose 
        going right instinctively. It's never let you down 
        so far. As you walk down the winding tunnel to the a
        right, the light rapidly disappears, and you begin 
        to forget where you started from. As you stumble around,
        beginning to feel hopeless, you start to be able to see
        a little ahead of you. You follow the light, until you
        reach an open ceiling cave, light pouring down onto a 
        single rock, upon which a woman sits. You approach.
        """)
        Light_Path_Two_Second_Paragraph()

    else:
        Light_Path_Two_Point_One_Option_Set_Input()

def Light_Path_Two_Point_One_Option_Set():
    typewriter("    You have two options:")
    time.sleep(0.5)
    typewriter("""
    A - Go left.
    """)
    time.sleep(0.5)
    typewriter("""
    B - Go right.
     """)

    Light_Path_Two_Point_One_Option_Set_Input()

def Light_Path_Two_First_Option_Set_Input():
    my_input = input("    Please type A or B:   ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        A - The cave is dark and damp, and you have 
        very little more than your wits in the way of 
        guidance. You come to a fork in the road.
        """)
        Light_Path_Two_Point_One_Option_Set()


    elif my_input_lower == "b":
        typewriter("""
        You walk further along the beach, before arriving to 
        sandy dunes. They lead to a cliffside ledge, where you see
        a figure sitting on a rock in the near distance. You approach.
        """)
        Light_Path_Two_Second_Paragraph()
     

    else:
        Light_Path_Two_First_Option_Set_Input()

def Light_Path_Two_First_Option_Set():
    typewriter("    You have two options:")
    time.sleep(0.5)
    typewriter("""
    A - There's a cave ahead of you. You decide to explore it.
    """)
    time.sleep(0.5)
    typewriter("""
    B - You decide to explore further along the coastline.
     """)
    Light_Path_Two_First_Option_Set_Input()


def Light_Path_Two_First_Paragraph():
    typewriter("""
    The salt air alerts you before you open your 
    eyes to where you are - the seaside. You open your 
    eyes, and see that you're within a sheltered 
    cove. You shudder. Beautiful places are the 
    favoured haunts of some of the most evil creatures.
    """)
    time.sleep(1)
    Light_Path_Two_First_Option_Set()

# ============================Light Path One Sequence=========================================================

def Light_Path_One_Death_Loop():

    my_input = input("""
    Would you like to begin again?  Please type yes or no: """)
    my_input_lower = my_input.lower()
    if my_input_lower == "yes":
        Light_Path_One_First_Paragraph()
    elif my_input_lower == "no":
        print_credits()
    else:
        Light_Path_One_Death_Loop()

def Light_Path_One_Second_Option_Set_Input():
    my_input = input("    Please type A or B:   ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        typewriter("""
        The closer you get, the hotter it gets. However, 
        you're only a couple steps away... you can make
        it...you reach out your hand and touch the handle
        on the top...and are frozen in place. A spell has 
        paralysed you, you can neither move forward nor 
        backwards. The concentrated heat of the sun cooks 
        you alive.
        """)

        time.sleep(1)

        print("    GAME OVER")
    
        Light_Path_One_Death_Loop()

    elif my_input_lower == "b":
        typewriter(""" 
        The closer you get, the hotter it gets. However, 
        you're only a couple steps away... you can make
        it...you reach out your hand and touch the latch
        at the front of the cage. It burns to the touch. 
        The pixie's eyes narrows then widens when you 
        release the latch. She flits out, and as she does 
        so, the light floods out of the atrium, returning 
        to the sky's domain. You blink, reajusting to the
        gloom of the castle. She stares at you for a moment,
        then leaves, without a glance back at you. You sigh.
        You must return to McGrumbles empty handed.
        """)
        time.sleep(1)
        typewriter("""
        You leave out the front door, which the pixie left 
        open. In the centre of the doorway is a vial - a 
        tiny vial. Upon examination, you realise the pixie 
        has left you a meagre amount of pixie dust, just
        the amount that you would need for McGrumbles. Not a
        huge thank you for providing her freedom, but it will
        do. 
        """)
        typewriter("""
        Armed with the vial, you make your way back to Celador.
        Once you're back, you'll only face one more challenge,
        before you can move on from this wretched affair. You're
        so close....
        """)
        light_end_story()
        
    else: Light_Path_One_Second_Option_Set_Input()


def Light_Path_One_Second_Option_Set():
    print("    You have two options:")
    time.sleep(0.5)
    typewriter("""
    A -  You survey the area for danger, and see none.
    You step forward, and can feel the heat of the light.
    You decide to take the pixie and leave this castle 
    forever.
    """)
    time.sleep(0.5)
    typewriter("""
    B - The pixie is the answer to all your needs, but you
    couldn't live with yourself if you enslaved such a 
    helpless creature. You decide to let her go.
     """)
    Light_Path_One_Second_Option_Set_Input()

def Light_Path_One_Second_Paragraph():
    typewriter("""
     You walk into the castle. You explore the out-
     skirts ground floor carefully, noting both its 
     splendor and emptiness. Having circled around 
     to where you began, you move towards the centre. 
     The shadows begin to recede the closer you get
     to the centre, and fear makes you pause. However,
     you start to understand the magic of this place - 
     the atrium is where the castle has stored the all 
     the light it has stolen from the sun, and it is 
     blinding. You try to block out the light with your 
     hands, but through your fingers, you see a pixie, 
     glaring hatefully at you through the bars of an 
     intricate bird cage. You know you have finally 
     arrived to what you have been looking for for years 
     - a pixie in a cage would be your slave, and could 
     act as a power source for the rest of your life.
    """)
    Light_Path_One_Second_Option_Set()


    

def Light_Path_One_First_Option_Set_Input():
    my_input = input("    Please type A or B:   ")
    my_input_lower = my_input.lower()
    if my_input_lower == "a":
        print("""
        You decide not to make yourself announced, 
        and head around the back to see if there's 
        a broken window you can climb through.
        """)

        Light_Path_One_Second_Paragraph()


    elif my_input_lower == "b":
        typewriter("""
        Curiosity humming through your veins, you slip through 
        the brambles and find yourself in the midst of a maze. 
        You smile to yourself, knowing that you've conquered 
        many such challenges before. Would this challenge be 
        as simple as finding the centre of a maze?
        """)
        
        time.sleep(1)
        
        typewriter("""
        You walk the walls of the maze for hours, your confidence 
        ebbing away slowly as you start to remember McGrumble's 
        final words to you, 'Don't get distracted...'
        """)

        time.sleep(1)

        typewriter("""
        You walk the paths of the cursed maze for eternity, 
        forever thinking over the decisions you made that 
        led you to this point...
        """)

        time.sleep(1)
        typewriter("""
        You are never seen again.
        """)

        time.sleep(1)

        typewriter("""
        GAME OVER
        """)

        Light_Path_One_Death_Loop()

    else:
        Light_Path_One_First_Option_Set_Input()

def Light_Path_One_First_Option_Set():
    typewriter("    You have two options:")
    time.sleep(0.5)
    typewriter("""
    A - You decide to search for another way into the castle.
    """)
    time.sleep(0.5)
    typewriter("""
    B - You decide to explore the walled garden to the right,
     which certainly looks like a place where a mystical item
     might be hidden...

     """)
    Light_Path_One_First_Option_Set_Input()

def Light_Path_One_First_Paragraph_Input():
    
    input("    Press enter to continue")
    typewriter("""
        Moving closer to the castle, you note with
        displeasure that the portcullis has been
        lowered, and that you certainly would not be
        entering from the front door, unless you wanted
        the castle inhabitants to know you were here. 
        You look around, unsure of what to do next. 
        'This would all be easier if McGrumbles had told 
        me what I was looking for', you think ruefully, 
        knowing it was not in McGrumble's character to 
        provide a single piece of information he didn't 
        have to...
        """)
    time.sleep(1)

    typewriter("""
        'Well, I have to get in there somehow....'
        
        """)
    Light_Path_One_First_Option_Set()

def Light_Path_One_First_Paragraph():

    typewriter("""
    You open your eyes. Ahead of you stands a towering castle, 
    ivy growing up the stone walls and disappearing into the many 
    crevices in its crumbling facade. You take in its ominous sight, 
    as McGrumble's last words to you echoed in your head; 'Don't get 
    distracted, head straight for the castle.' Even though you knew 
    it should have been full noon, it almost seemed like dusk, and it 
    became darker with every step closer to the towers. You think 
    to yourself this must be a dangerous place if the castle dared to 
    steal the sun's light during its day reign.
    """)
    time.sleep(1)
    Light_Path_One_First_Paragraph_Input()


# Light_Path_One_First_Paragraph()
# Light_Path_One_Second_Option_Set_Input()


# #================================================================ Light random choice/paths =========================
#====Kept for griffin attack possible use ===========

# def light_path_one():
#     print("light path one go!!!!")
# #     light_path_one_choice = input("a or b ")
# #     if light_path_one_choice == "a":
# #         print("you die")
# #         light_path_random_choice()
# #     elif light_path_one_choice == "b":
# #         print("you have won the first challenge!!!!")
# #         random_num_light_path_one = random.randint(0,2)
# #         random_griffin_attack = 0
# #         if random_num_light_path_one == random_griffin_attack:
# #             print("you hear a whooshing noise above the trees...")
# #             fight_the_griffin()
# #         else:
# #             light_path_random_choice_two()
# =================================================




def light_path_random_choice():

    typewriter("""
    In the beginning, you chose the light path because it was a magical path free from restriction, allowing you to 
    chase your destiny... or so you thought. You have always known that finding the white unicorn of Celador, a 
    mystical creature famed for the power to heal, has been your life's purpose.""")

    print("")

    typewriter("""
    But those light wizards! Obsessed with their rules, keeping you from your destiny! And so, you started your search, 
    many leagues from the Kingdom of Escherton, pledging to wander until you found the one that you 
    seek...the one that can help you...""")
    
    print(" ")

    typewriter("""
    ...the one known only as McGrumbles..."""  )

    print("")

    typewriter("""
    'And so, you have found yourself in the Glade of Ill Portends!' McGrumbles towers above you. 'You are here seeking 
    adventure. Ha Ha! THAT is definately something that I can help you with....'""")

    print(" ")

    typewriter("""
    McGrumbles reaches for his wand and points it directly at you.""")
 
    print("")
  
    typewriter("""
    'Where you will find yourself, I do not know...'""")

    print(" ")

    typewriter("""
    You find yourself spinning in a vortex the like of which you have not seen before...""")

    print(" ")
    
    time.sleep(2)

    typewriter("""
    Who knows where you will land...""")

    print(" ")

    time.sleep(2)
    print("")

    vortex_adjective_list = ["    Swirling", "    Stars", "    What's that!"]

    vortex_index_count = 0
    for x in vortex_adjective_list:
        print(x)
        print(" ")
        time.sleep(3)
        
    light_path_choice_list = [Light_Path_One_First_Paragraph, Light_Path_Two_First_Paragraph]
    random.choice(light_path_choice_list)()
    # Light_Path_One_First_Paragraph()

#=================================================================================================================================

#===================================================================== Intro functions ============================================

def game_intro():
    typewriter("""
    WELCOME, young wizard, and behold the majesty of the Kingdom of Escherton, the ancient and most powerful realm of 
    wizards! Famed from the Six Seas of Sulphur to the mighty Walls of the Tiberian Empire, the Kingdom of Escherton
    is here to offer you a bright and shinning future! Having just finished your studies at Magic University, you are 
    ready to begin your career as a spellcaster.""")
    os.system()
    # time.sleep(2)

    print("")
    
    typewriter( """
    But, before you can start with your magical career, we need to know a little about you. Firstly, by what name do you go? """)

    print("")

    # time.sleep(2)
     
    name_input = input("    Enter your name: ")
    name_input_lower = name_input.lower()
    global name_input_capitalize
    name_input_capitalize = name_input_lower.capitalize() 
    print(" ")  
    time.sleep(0.5)

    typewriter(f"""
    Welcome {name_input_capitalize}, what were your studies at Magic University? Are you a Light wizard, or are you Dark?""")

    print("")
    
    color_input = input("    Enter your wizard type - light or dark: ")
    global color_input_lower
    color_input_lower = color_input.lower()

    # global new_wizard
    # new_wizard.name = name_input_capitalize
    # new_wizard.color = color_input_lower

    if color_input_lower == "dark":
        time.sleep(1)
        typewriter(f"    The dark path awaits you, {name_input_capitalize}...")
        print(" ")
        i = 5
        while i > 0:
            print("    " + str(i))
            time.sleep(1)
            i = i - 1
        dark_path_random_choice()   

    elif color_input_lower == "light":  
        time.sleep(1)    
        typewriter(f"""
        The light path awaits you, {name_input_capitalize}...""")  
        print(" ")
        i = 5
        while i > 0:
            print("    " + str(i))
            time.sleep(1)
            i = i - 1
        light_path_random_choice()
    else:
        print("")
        typewriter("    Wizards must be able to spell... it's back to the beginning for you!")    
        print("")
        game_intro()

game_intro()


#=================================================================================================================================
