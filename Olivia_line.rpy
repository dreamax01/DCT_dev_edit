#-----------------------------Olivia---------------------------------------------
label olivia_1:
    call interface from _call_interface_27
    show fit_exit_idle
    pause (0.01)
    image olivia_1_promo ='images/characters/olivia/oli_1/olivia_1_promo.jpg'
    scene olivia_1_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
    with dissolve
    scene olivia_1_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
        linear 8.0 xpos 0 ypos 0
    $ renpy.pause(7.0, hard='True')
    olivia "Good afternoon, welcome to our fitness center."
    olivia "Can I help you?"
    image olivia_1_2 ='images/characters/olivia/oli_1/olivia_1_2.jpg'
    scene olivia_1_2
    j "Yes, I recently moved here and now I live close by."
    j "I would like to know if there is an opportunity to get a job?"
    image olivia_1_3 ='images/characters/olivia/oli_1/olivia_1_3.jpg'
    scene olivia_1_3
    olivia "This is great, what is your education?"
    image olivia_1_4 ='images/characters/olivia/oli_1/olivia_1_4.jpg'
    scene olivia_1_4
    j "I graduated from MILF University."
    image olivia_1_7 ='images/characters/olivia/oli_1/olivia_1_7.jpg'
    scene olivia_1_7
    j "(And she has great legs ...)"
    image olivia_1_5 ='images/characters/olivia/oli_1/olivia_1_5.jpg'
    scene olivia_1_5
    olivia "(Where he's looking, I hope my skirt isn't too short.)"
    olivia "In this case, we do have a free vacancy, how about being a bartender?"
    j "I'm okay with that! It does not seem like a complicated job."
    image olivia_1_8 ='images/characters/olivia/oli_1/olivia_1_8.jpg'
    scene olivia_1_8
    olivia "I can handle any work there"
    olivia "But do keep in mind that this is an elite fitness center and customers have certain levels of expectations."
    olivia "They can concoct their own cocktail recipe, so do not rely on remembering the same combinations."
    olivia "Any mistake during the working day and you will be left without money."
    olivia "I will pay you a salary after each shift."
    olivia "Since we still don't know anything about you, we will arrange for you to do an intership, in which you'll prove your worth."
    scene olivia_1_4
    j "(Hmm, those are some harsh conditions, I hope everything works out.)"
    j "Ok, I will try."
    olivia "Great, then you are accepted into our wonderful team."
    olivia "And remember our slogan: Dreams must be sustainable."
    j "(God, I've never heard anything more stupid in my life.)"
    j "What a wonderful slogan."
    image olivia_1_9 ='images/characters/olivia/oli_1/olivia_1_9.jpg'
    scene olivia_1_9
    olivia "So, officially we will hand you an internship, for now I just need your phone number."
    olivia "Remember that your further career growth depends on mutual understanding."
    olivia "Work clothes will be given to you."
    j "Thank you so much."
    scene olivia_1_2
    olivia "You can work at any time that is convenient to you, starting from 09:00."
    olivia "The salary is $ 10 per shift and tip, this is an internship."
    olivia "To continue working with us past the intership, you'll have to work hard."
    j "I realised I forgot to ask, but how long would my internship last?"
    olivia "Depends on your diligence and developer. Good luck."

    scene oli_3
    $ hide_interface = False
    $ olivia_1_comp = True
    $ inventory.drop_task(task_find_job_fit)
    $ inventory.add_task(task_work_at_bar)
    $ new_task = True
    $ renpy.block_rollback()
    jump fit_exit
    return

label olivia_2:
    call interface from _call_interface_28
    show fit_exit_idle
    scene olivia_1_1 with dissolve
    if day_time < 4:
        olivia "Hello, you can get to work."
        menu:
            "Work as a bartender":
                if work_bar_already == True:
                    olivia "You already worked your shift."
                    $ hide_interface = False
                    jump fit_exit
                jump work_fit_bar
            "Cancel":
                $ hide_interface = False
                jump fit_exit
    else:
        olivia "Hello, did you want something?"
        j "Do not bother me when I'm working.."
        scene olivia_1_2
        olivia "Do not bother me when I'm working."
        $ hide_interface = False
        jump fit_exit

label olivia_3:
    scene olivia_1_1
    "[olivia] meets me after work"
    olivia "Hi, I wanted to talk with you, let's go to my office."
    j "(I think I should not refuse her offer.)"
    image olivia_3_1 ='images/characters/olivia/oli_3/olivia_3_1.jpg'
    scene olivia_3_1 with fade
    olivia "Come in, this is my office, here we can solve all our problems."
    image olivia_3_2 ='images/characters/olivia/oli_3/olivia_3_2.jpg'
    scene olivia_3_2
    olivia "Relax, We're not here to fire you. On the flipside, I wanted to talk to you about pleasant things."
    image olivia_3_3 ='images/characters/olivia/oli_3/olivia_3_3.jpg'
    scene olivia_3_3
    olivia "I have analyzed your results here and I see you have great potential."
    image olivia_3_4 ='images/characters/olivia/oli_3/olivia_3_4.jpg'
    scene olivia_3_4
    olivia "Want to earn more than what you're earning now?"
    image olivia_3_5 ='images/characters/olivia/oli_3/olivia_3_5.jpg'
    scene olivia_3_5
    j "Of course, money is always needed."
    scene olivia_3_4
    olivia "I thought that you would be happy to hear my proposal."
    olivia "You must understand that this is not an easy job."
    image olivia_3_6 ='images/characters/olivia/oli_3/olivia_3_6.jpg'
    scene olivia_3_6
    olivia "Since we are an elite fitness center, many popular personalities come to us."
    image olivia_3_7 ='images/characters/olivia/oli_3/olivia_3_7.jpg'
    scene olivia_3_7
    olivia "It’s a sin not to take the opportunity to capture them naked."
    image olivia_3_8 ='images/characters/olivia/oli_3/olivia_3_8.jpg'
    scene olivia_3_8
    olivia "You don't have to worry, no one can prove that we are doing this."
    olivia "Well, these photos are expensive, but to get them, you need to monitor and photograph the victim so that she does not notice."
    image olivia_3_9 ='images/characters/olivia/oli_3/olivia_3_9.jpg'
    scene olivia_3_9
    olivia "If you are noticed, then I will deny everything."
    image olivia_3_10 ='images/characters/olivia/oli_3/olivia_3_10.jpg'
    scene olivia_3_10
    olivia "And I will deduct the moral payment of the victim from your salary.."
    j "I can try but I can't promise that I will succeed."
    image olivia_3_11 ='images/characters/olivia/oli_3/olivia_3_11.jpg'
    scene olivia_3_11
    olivia "Having worked so many shifts in the bar, you showed excellent attentiveness."
    image olivia_3_12 ='images/characters/olivia/oli_3/olivia_3_12.jpg'
    scene olivia_3_12
    olivia "And if you manage to bring me high-quality photographs of clients, then perhaps you will get not only money and promotion."
    image olivia_3_13 ='images/characters/olivia/oli_3/olivia_3_13.jpg'
    scene olivia_3_13
    j "(What's wrong with her... She has never came this close to me before.)"
    j "Ok, I'll try."
    olivia "It’s good that we agreed."
    scene olivia_3_13
    olivia "I think you understand that it is better not to tell anyone about this conversation."
    olivia "Good luck to you!"
    image olivia_3_15 = Movie(play="images/characters/olivia/oli_3/olivia_3_15.webm")
    scene olivia_3_15 with fade
    pause(10)
    image olivia_3_14 ='images/characters/olivia/oli_3/olivia_3_14.jpg'
    scene olivia_3_14
    olivia "I hope you and I will have a fruitful partnership."
    image olivia_3_16 ='images/characters/olivia/oli_3/olivia_3_16.jpg'
    scene olivia_3_16
    j "(I think I need a good camera.)"
    j "(God, she has a ring on. She's married and she lets herself do that?!)"

    scene olivia_3_14
    $ renpy.end_replay()
    $ hide_interface = False
    $ olivia_3_comp = True
    $ inventory.drop_task(task_work_at_bar)
    $ inventory.add_task(task_purch_dig_cam)
    $ new_task = True
    $ renpy.block_rollback()
    jump fit_exit
