#-----------------------------Sandy_sleep_bad--------------------------------------------
label label_sandy_sleep:
    if was_sandy_room_night == False:
        call interface from _call_interface_22
        image int_sandy_sleep = "images/gg_house/sandy_room/scenes/int_sandy_sleep.jpg"
        scene int_sandy_sleep
        j "([sandy] is sleeping so sweetly)"
        j "I really want to take a closer look, but I can't make too much noise."
        image int_sandy_sleep_nude = "images/gg_house/sandy_room/scenes/int_sandy_sleep_nude.jpg"
        scene int_sandy_sleep_nude with dissolve
        j "Wow! Look at her curves!"
        call screen sandy_sleep_zone
screen sandy_sleep_zone:
    zorder 1
    add "images/game_gui/icons/sex_icons/zone_sandy.png" xalign 0.5 yalign 0.03 zoom 1.5
    imagebutton:
        xalign 0.97
        yalign 0.97
        focus_mask True
        idle Transform("images/game_gui/buttons/back_idle.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/buttons/back_idle.png",im.matrix.brightness(0.05)), zoom=.35)
        if clickable == True:
            action [Hide("displayTextScreen"),SetVariable("hide_interface", False),Jump('label_sandy_room')]
    imagebutton:
        xalign 0.03
        yalign 0.97
        focus_mask True
        idle Transform("images/game_gui/buttons/button_wakeup.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/buttons/button_wakeup.png",im.matrix.brightness(0.05)), zoom=.35)
        if clickable == True:
            action [Hide("displayTextScreen"), Show('work_in_progress')]
    imagebutton:
        xpos 1560
        ypos 230
        focus_mask True
        idle Transform("images/game_gui/icons/sex_icons/button_star.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/icons/sex_icons/button_star.png",im.matrix.brightness(0.05)), zoom=.35)
        action [Hide("sandy_sleep_zone"),Hide("displayTextScreen"), Call('sandy_night_mouth')]
        hovered Show("displayTextScreen", displayText = "Mouth")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1319
        ypos 170
        focus_mask True
        idle Transform("images/game_gui/icons/sex_icons/button_star.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/icons/sex_icons/button_star.png",im.matrix.brightness(0.05)), zoom=.35)
        action [Hide("sandy_sleep_zone"),Hide("displayTextScreen"), Call('sandy_night_tits')]
        hovered Show("displayTextScreen", displayText = "Tits")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 1022
        ypos 320
        focus_mask True
        idle Transform("images/game_gui/icons/sex_icons/button_cl_star.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/icons/sex_icons/button_cl_star.png",im.matrix.brightness(0.05)), zoom=.35)
        action [Hide("displayTextScreen"), Show('work_in_progress')]
        hovered Show("displayTextScreen", displayText = "Pussy")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xpos 190
        ypos 720
        focus_mask True
        idle Transform("images/game_gui/icons/sex_icons/button_cl_star.png", zoom=.35)
        hover Transform(im.MatrixColor("images/game_gui/icons/sex_icons/button_cl_star.png",im.matrix.brightness(0.05)), zoom=.35)
        action [Hide("displayTextScreen"), Show('work_in_progress')]
        hovered Show("displayTextScreen", displayText = "Feet")
        unhovered Hide("displayTextScreen")

label sandy_1:
    call interface from _call_interface_23
    $ renpy.block_rollback()
    show gg_sandy_room_hover
    if sandy_1_comp == True:
        image sandy_1_2 ='images/characters/sandy/sandy_1/sandy_1_2.jpg'
        scene sandy_1_2
        sandy "Now wait a second."
        scene sandy_1_5
        sandy "Don't bother me! Go and help me get the answers for the exams!"
        j "I'm leaving."
        $ renpy.end_replay()
        $ hide_interface = False
        jump label_hall_room
    pause (0.01)
    image sandy_1_promo ='images/characters/sandy/sandy_1/sandy_1_1_promo.jpg'
    scene sandy_1_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
    with dissolve
    scene sandy_1_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
        linear 8.0 xpos 0 ypos 0
    $ renpy.pause(7.0, hard='True')
    j "Hi, am I bothering you?"
    image sandy_1_2 ='images/characters/sandy/sandy_1/sandy_1_2.jpg'
    scene sandy_1_2
    sandy "Actually, you're disturbing me with your presence."
    sandy "But what did you want?"
    sandy "...I'll call you back..."
    image sandy_1_5 ='images/characters/sandy/sandy_1/sandy_1_5.jpg'
    scene sandy_1_5 with fade
    j "I wanted to know how you're doing, we haven't met in a long time."
    sandy "It's okay, but I'm very busy right now, I have exams soon."
    j "Hah, okay, then why aren't you getting ready for them?"
    image sandy_1_8 ='images/characters/sandy/sandy_1/sandy_1_8.jpg'
    scene sandy_1_8
    sandy "Very funny, did you come here to mock me?"
    j "No, okay, I won’t bother you."
    image sandy_1_12 ='images/characters/sandy/sandy_1/sandy_1_12.jpg'
    scene sandy_1_12
    sandy "Wait, sorry..."
    scene sandy_1_8
    j "I understand that you need to prepare, can I help you with exams somehow?"
    image sandy_1_9 ='images/characters/sandy/sandy_1/sandy_1_9.jpg'
    scene sandy_1_9
    sandy "Forget it, it's not really important."
    j "But still, say it."
    image sandy_1_13 ='images/characters/sandy/sandy_1/sandy_1_13.jpg'
    scene sandy_1_13
    sandy "Only if you got the answers to all the exams, then maybe..."
    sandy "In total, I have 7 exams, the answers to 3 of them are stored at school, I don’t know about the rest."
    sandy "Try to get these three and I'll figure out how to thank you."
    sandy "And of course, we can resell them and make some money."
    sandy "I always knew that I had business skills."
    scene sandy_1_9
    j "It seems very difficult."
    j "How can I get answers when there are so many people there and everyone will notice?"
    scene sandy_1_8
    sandy "I know that nobody is there at night."
    j "(And she looks smart ...)"
    sandy "You didn't hear about this from me, but I got in with my friends through the back door."
    j "I'll try."
    image sandy_1_14 ='images/characters/sandy/sandy_1/sandy_1_14.jpg'
    scene sandy_1_14
    sandy "I really hope that you will succeed, but for now I'll just prepare for the exams."
    sandy "We'll talk when you got something."
    sandy "You can find me either at home or at school."
    j "(Now I need to find out what exams she needs to take.)"
    j "(Unfortunately, she is not very talkative yet, I think if I get at least some answers, it will help.)"
    j "(You can’t look at school during the day, so you have to climb there at night.)"
    j "(I definitely need a flashlight and a fake key.)"
    j "(I can buy a flashlight in the store, but faking the key will be more difficult.)"
    j "(We'll need to talk to my friend, [frank].)"

    $ renpy.end_replay()
    $ hide_interface = False
    $ sandy_1_comp = True
    $ new_task = True
    $ inventory.drop_task(task_talk_sandy)
    if not flashlight in inventory.items:
        $ inventory.add_task(task_purch_flashlight)
    $ inventory.add_task(task_talk_frank)
    jump label_hall_room

label sandy_2:
    call interface from _call_interface_58
    show school_exit_idle
    pause (0.01)
    image sandy_school_promo ='images/characters/sandy/sandy_2/sandy_school_promo.jpg'
    scene sandy_school_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
    with dissolve
    scene sandy_school_promo:
        zoom 1
        xanchor 0 yanchor 0 xpos 0 ypos -2700
        linear 8.0 xpos 0 ypos 0
    $ renpy.pause(7.0, hard='True')
    j "Hi, are you busy?"
    image sandy_2_1 ='images/characters/sandy/sandy_2/sandy_2_1.jpg'
    scene sandy_2_1
    pause(1)
    image sandy_2_2 ='images/characters/sandy/sandy_2/sandy_2_2.jpg'
    scene sandy_2_2 with dissolve
    sandy "Hi, everybody's thinking how to pass this damn exam."
    j "You were preparing! You can do it!"
    image sandy_2_3 ='images/characters/sandy/sandy_2/sandy_2_3.jpg'
    scene sandy_2_3
    sandy "Thank you for your support, but I clearly need help with this."
    jump sandy_2_menu
label sandy_2_menu:
    image sandy_2_3_1 ='images/characters/sandy/sandy_2/sandy_2_3_1.jpg'
    scene sandy_2_3_1
    menu:
        "Who are you talking to?":
            j "Can I ask who's the person you're always on the phone with?"
            image sandy_2_4_1 ='images/characters/sandy/sandy_2/sandy_2_4_1.jpg'
            scene sandy_2_4_1
            sandy "If I didn't need your help, I wouldn't tell you, but now I need it."
            image sandy_2_5_1 ='images/characters/sandy/sandy_2/sandy_2_5_1.jpg'
            scene sandy_2_5_1
            sandy "I'm talking to [jane], she's my friend."
            sandy "She's taking the exam alongside me."
            j "So why don't you ask her to help you?"
            image sandy_2_6 ='images/characters/sandy/sandy_2/sandy_2_6.jpg'
            scene sandy_2_6
            sandy "You do not know her."
            sandy "She's obsessed with dancing, she doesn't care for any exams."
            image sandy_2_7 ='images/characters/sandy/sandy_2/sandy_2_7.jpg'
            scene sandy_2_7
            sandy "But it's only a test, she's still my good friend"
            j "I haven't seen both of you together yet, do you guys only talk through the phone?"
            image sandy_2_8 ='images/characters/sandy/sandy_2/sandy_2_8.jpg'
            scene sandy_2_8 with dissolve
            sandy "We're both busy these days, so we're only able to afford communicating through the phone."
            image sandy_2_10 ='images/characters/sandy/sandy_2/sandy_2_10.jpg'
            scene sandy_2_10
            sandy "But I think that we'll have more time after passing the test."
            image sandy_2_9 ='images/characters/sandy/sandy_2/sandy_2_9.jpg'
            scene sandy_2_9
            j "I think it will be so."
            jump sandy_2_menu
        "You have to prepare yourself.":
            j "You have to prepare yourself"
            image sandy_2_4 ='images/characters/sandy/sandy_2/sandy_2_4.jpg'
            scene sandy_2_4
            sandy "Pfft, you think I didn't try?"
            sandy "Whatever I do, I always go wrong with this test."
            image sandy_2_5 ='images/characters/sandy/sandy_2/sandy_2_5.jpg'
            scene sandy_2_5
            sandy "The only way to go through it is to get answers."
            j "But what if you tried studying and passing it all by yourself?"
            image sandy_2_11 ='images/characters/sandy/sandy_2/sandy_2_11.jpg'
            scene sandy_2_11
            sandy "Then, if I don’t give up, you yourself will explain to [megan] why I didn’t succeed."
            sandy "And I will tell her that you refused to help me."
            image sandy_2_13 ='images/characters/sandy/sandy_2/sandy_2_13.jpg'
            scene sandy_2_13
            sandy "But I'm not the kind of bitch to blackmail you."
            image sandy_2_16 ='images/characters/sandy/sandy_2/sandy_2_16.jpg'
            scene sandy_2_16
            sandy "I think you have enough conscience to help me."
            image sandy_2_10 ='images/characters/sandy/sandy_2/sandy_2_10.jpg'
            scene sandy_2_10
            j "It feels like it all comes down to one thing."
            j "At first they ask me in an amicable way, and then it begins ..."
            j "Nevermind…"
            jump sandy_2_menu
        "I will try to help you prepare.":
            j "I will try to help you prepare."
            image sandy_2_5_1 ='images/characters/sandy/sandy_2/sandy_2_5_1.jpg'
            scene sandy_2_5_1
            sandy "That would be great, but I don't need your knowledge."
            image sandy_2_6 ='images/characters/sandy/sandy_2/sandy_2_6.jpg'
            scene sandy_2_6
            sandy "And I need specific answers."
            sandy "Get them for me and I'll owe you."
            j "I don't need anything from you."
            image sandy_2_7 ='images/characters/sandy/sandy_2/sandy_2_7.jpg'
            scene sandy_2_7
            sandy "You don't have to pretend, you're a guy after all. I can- I will help you."
            image sandy_2_8 ='images/characters/sandy/sandy_2/sandy_2_8.jpg'
            scene sandy_2_8
            sandy "Maybe you can help me in a way for the test other than studying for it?"
            j "We'll see."
            $ sandy_2_comp = True
            jump sandy_2_menu
        "Tell me about [jane].":
            j "Tell me about [jane]."
            image sandy_2_9 ='images/characters/sandy/sandy_2/sandy_2_9.jpg'
            scene sandy_2_9
            sandy "I'll tell you about her once you bring me the answers."
            j "Why so secretive?"
            image sandy_2_14 ='images/characters/sandy/sandy_2/sandy_2_14.jpg'
            scene sandy_2_14
            sandy "Look, if you're so interested in her... I'll tell you, but..."
            image sandy_2_15 ='images/characters/sandy/sandy_2/sandy_2_15.jpg'
            scene sandy_2_15
            sandy "Get it done first."
            image sandy_2_16 ='images/characters/sandy/sandy_2/sandy_2_16.jpg'
            scene sandy_2_16
            sandy "You must have some kind of incentive ..."
            jump sandy_2_menu
        "Go away.":
            j "See you, [sandy]."
            sandy "Bye dear."
            $ hide_interface = False
            jump school_exit

label sandy_3:
    call interface from _call_interface_60
    $ renpy.block_rollback()
    show gg_living_room_idle
    image sandy_3_1 ='images/characters/sandy/sandy_3/sandy_3_1.jpg'
    scene sandy_3_1 with fade
    "([sandy] is watching TV.)"
    j "[sandy], hello!"
    j "Can we talk?"
    image sandy_3_3 ='images/characters/sandy/sandy_3/sandy_3_3.jpg'
    scene sandy_3_3
    sandy "Of course, I was just waiting for you."
    sandy "You don't seem to be in much of a hurry."
    image sandy_3_4 ='images/characters/sandy/sandy_3/sandy_3_4.jpg'
    scene sandy_3_4
    sandy "That's right, take a seat."
    sandy "We're living together now."
    image sandy_3_5 ='images/characters/sandy/sandy_3/sandy_3_5.jpg'
    scene sandy_3_5
    j "Do you like watching Fashion Shows?"
    image sandy_3_7 ='images/characters/sandy/sandy_3/sandy_3_7.jpg'
    scene sandy_3_7
    sandy "Yeah, it helps me relax from all the studying I've been doing for the exams."
    image sandy_3_6 ='images/characters/sandy/sandy_3/sandy_3_6.jpg'
    scene sandy_3_6 with dissolve
    sandy "..."
    image sandy_3_8 ='images/characters/sandy/sandy_3/sandy_3_8.jpg'
    scene sandy_3_8
    j "Maybe you should go for a walk with your friends or someone else?"
    image sandy_3_9 ='images/characters/sandy/sandy_3/sandy_3_9.jpg'
    scene sandy_3_9
    sandy "[j], I'll think about your proposal, but so far I have only one in my head."
    image sandy_3_10 ='images/characters/sandy/sandy_3/sandy_3_10.jpg'
    scene sandy_3_10
    sandy "Tell me please."
    sandy "You got the answers, didn't you?"
    image sandy_3_12 ='images/characters/sandy/sandy_3/sandy_3_12.jpg'
    scene sandy_3_12
    j "Yes, is it this?"
    sandy "Unfortunately yes."
    j "Why aren't you happy?"
    image sandy_3_14 ='images/characters/sandy/sandy_3/sandy_3_14.jpg'
    scene sandy_3_14
    sandy "Because you decided to bring me the original copy and we are very lucky that they somehow haven't found out yet."
    image sandy_3_13 ='images/characters/sandy/sandy_3/sandy_3_13.jpg'
    scene sandy_3_13
    sandy "So next time, just take a picture."
    j "Fuck, you're right."
    j "What do I do now?"
    image sandy_3_15 ='images/characters/sandy/sandy_3/sandy_3_15.jpg'
    scene sandy_3_15
    sandy "You need to get them back in the original location as soon as possible before anyone finds out it was even gone!"
    j "Sorry there was a guard patrolling and I didn't have time to take a picture of the answers."
    image sandy_3_16 ='images/characters/sandy/sandy_3/sandy_3_16.jpg'
    scene sandy_3_16
    sandy "I'm not sure if this helps, but hey it's better than nothing right!"
    image sandy_3_17 ='images/characters/sandy/sandy_3/sandy_3_17.jpg'
    scene sandy_3_17
    sandy "Thanks, [j]."
    sandy "At least you tried."
    j "Let's talk again after I returned the answers back."
    sandy "Okay."
    sandy "And [j], be careful."
    j "Don't worry."
    image sandy_3_18 ='images/characters/sandy/sandy_3/sandy_3_18.jpg'
    scene sandy_3_18
    "(Sandy went to the bathroom.)"
    j "(Her ass is beautiful.)"
    image sandy_3_19 ='images/characters/sandy/sandy_3/sandy_3_19.jpg'
    scene sandy_3_19
    j "Hmm, she left her phone here. Maybe I should take a look."
    $ hide_interface = False
    $ sandy_3_comp = True
    $ inventory.drop_task(task_give_answer_1)
    $ inventory.add_task(task_return_answer_1)
    $ new_task = True
    $ renpy.block_rollback()
    jump label_living_room
    return
label sandy_4:
    call interface from _call_interface_61
    $ renpy.block_rollback()
    show gg_living_room_idle
    image sandy_4_1 ='images/characters/sandy/sandy_4/sandy_4_1.jpg'
    scene sandy_4_1 with fade
    j "(Great, Sandy is in the bathroom now.)"
    j "(So, let's see what we have here.)"
    j "(Damn it, she has a password here.)"
    image sandy_4_2 ='images/characters/sandy/sandy_4/sandy_4_2.jpg'
    scene sandy_4_2
    sandy "(Damn, I thought so!)"
    sandy "(I've only just left the phone, and [j] is already trying to unlock it!)"
    image sandy_4_3 ='images/characters/sandy/sandy_4/sandy_4_3.jpg'
    scene sandy_4_3
    sandy "(I didn't expect such impudence from him.)"
    sandy "(I'll have to talk to him about this.)"
    scene sandy_4_1
    j "(I will need to find out the password for her phone somehow.)"
    j "(She always complains about her memory.)"
    j "(She probably wrote down the password and left it in her room.)"
    $ hide_interface = False
    $ sandy_4_comp = True
    $ inventory.add_task(task_find_phone_pass)
    $ new_task = True
    $ renpy.block_rollback()
    jump label_living_room
    return
label sandy_5:
    call interface from _call_interface_62
    $ renpy.block_rollback()
    image sandy_5_1 ='images/characters/sandy/sandy_5/sandy_5_1.jpg'
    scene sandy_5_1
    menu:
        "{color=#4fb100}Start searching{/color}":
            jump sandy_r_5
        "Cancel":
            $ hide_interface = False
            jump label_sandy_room

label sandy_r_5:
    $ renpy.block_rollback()
    image sandy_5_1 ='images/characters/sandy/sandy_5/sandy_5_1.jpg'
    scene sandy_5_1
    j "([sandy] is showering now, you take the chance to look for her phone password.)"
    j "(It is unlikely that she did not write it down, it must have been in some kind of notebook.)"
    image sandy_5_2 ='images/characters/sandy/sandy_5/sandy_5_2.jpg'
    scene sandy_5_2
    j "(Let's see in her backpack.)"
    image sandy_5_3 ='images/characters/sandy/sandy_5/sandy_5_3.jpg'
    scene sandy_5_3
    j "(Oh great! It's right here!)"
    j "(Hmm, the password is 6969)."
    j "(I hope there is no hidden meaning here.)"
    image sandy_5_4 ='images/characters/sandy/sandy_5/sandy_5_4.jpg'
    scene sandy_5_4
    j "(Damnit! I can hear her walking back, I really don't want her catching me here!)"
    if megan_0_3_comp == True:
        j "(I've got experience hiding in closets, but now hers is too dangerous to climb into!)"
    else:
        j "(Need to think of something, maybe hide in the closet? No, it's a bad idea.)"
        j "(Moreover, there is only one door and if she doesn’t open it, she will immediately find me.)"
    image sandy_5_5 ='images/characters/sandy/sandy_5/sandy_5_5.jpg'
    scene sandy_5_5
    j "(I'd better hide under her bed, she's unlikely to look there.)"
    image sandy_5_6 ='images/characters/sandy/sandy_5/sandy_5_6.jpg'
    scene sandy_5_6
    sandy "What could be better than a relaxing shower?"
    sandy "Hmm, I think I know what could be better."
    image sandy_5_7 ='images/characters/sandy/sandy_5/sandy_5_7.jpg'
    scene sandy_5_7
    sandy "How sweet, its a shame that I have such dirty thoughts."
    sandy "It's good that my phone is password-protected. I don't want him seeing all my photos!"
    sandy "Today I'll delete everything so that he would never see it."
    j "(Damn, she seems to have seen me take her phone, so there is no point in the password.)"
    j "(But on the other hand, she has a very strange password.)"
    image sandy_5_8 ='images/characters/sandy/sandy_5/sandy_5_8.jpg'
    scene sandy_5_8
    sandy "Exams are coming soon, but I need to somehow relieve fatigue."
    image sandy_5_9 ='images/characters/sandy/sandy_5/sandy_5_9.jpg'
    scene sandy_5_9
    sandy "I have an idea."
    sandy "So where are you my dear?"
    image sandy_5_10 ='images/characters/sandy/sandy_5/sandy_5_10.jpg'
    scene sandy_5_10
    sandy "Here you are, how long we have been together, to be honest, I'm tired of you already."
    image sandy_5_11 ='images/characters/sandy/sandy_5/sandy_5_11.jpg'
    scene sandy_5_11
    sandy "Ok now I just need to close the doors and dim the lights. I love the romantic atmosphere."
    image sandy_5_12 ='images/characters/sandy/sandy_5/sandy_5_12.jpg'
    scene sandy_5_12
    j "(Damn what is going on! Has she really decided to pleasure herself this very moment, when I'm right underneath her bed?!)"
    image sandy_5_13 ='images/characters/sandy/sandy_5/sandy_5_13.jpg'
    scene sandy_5_13 with fade
    j "(I can't see very well from here, but she has amazing curves.)"
    image sandy_5_14 ='images/characters/sandy/sandy_5/sandy_5_14.jpg'
    scene sandy_5_14
    sandy "Alright, I'll pass the exams and find myself a guy who would fuck me good."
    j "(What is she up to?)"
    image sandy_5_15 ='images/characters/sandy/sandy_5/sandy_5_15.jpg'
    scene sandy_5_15
    sandy "Yeah, [j], kiss me!"
    image sandy_5_16 ='images/characters/sandy/sandy_5/sandy_5_16.jpg'
    scene sandy_5_16
    sandy "Caress me there, my dear."
    j "(What?! Is she fantasizing about me?)"
    image sandy_5_17 ='images/characters/sandy/sandy_5/sandy_5_17.jpg'
    scene sandy_5_17
    sandy "Show me how gentle you are."
    sandy "I'm really starting to enjoy this, im getting really wet."
    image sandy_5_18 ='images/characters/sandy/sandy_5/sandy_5_18.jpg'
    scene sandy_5_18
    sandy "Pleasure me with your big strong hands!"
    image sandy_5_19 = Movie(play="images/characters/sandy/sandy_5/sandy_5_19.webm")
    scene sandy_5_19 with fade
    pause(10)
    sandy "Yes, take your time, I won't run anywhere."
    j "(I'm certainly not going to get out of here.)"
    image sandy_5_20 ='images/characters/sandy/sandy_5/sandy_5_20.jpg'
    scene sandy_5_20
    sandy "Ahh I'm so wet all my juices are flowing out."
    sandy "Get your cock out."
    image sandy_5_21 ='images/characters/sandy/sandy_5/sandy_5_21.jpg'
    scene sandy_5_21
    sandy "Here you are, my dear."
    sandy "It's time for you to meet my vagina."
    image sandy_5_23 = Movie(play="images/characters/sandy/sandy_5/sandy_5_23.webm")
    scene sandy_5_23 with fade
    pause(10)
    sandy "Just like clockwork."
    sandy "You just have a wonderful dick."
    image sandy_5_24 ='images/characters/sandy/sandy_5/sandy_5_24.jpg'
    scene sandy_5_24
    j "(This is really hard to listen to. I just want to get out there and give her the real deal.)"
    image sandy_5_25 ='images/characters/sandy/sandy_5/sandy_5_25.jpg'
    scene sandy_5_25
    sandy "Oh [j]! You're so fired up today!."
    sandy "And I like your thoughts."
    j "(No doubt.)"
    image sandy_5_26 ='images/characters/sandy/sandy_5/sandy_5_26.jpg'
    scene sandy_5_26
    sandy "Come on, stick it deeper into me, because I’m your bad girl ..."
    sandy "I am not preparing for exams at all."
    image sandy_5_27 ='images/characters/sandy/sandy_5/sandy_5_27.jpg'
    scene sandy_5_27
    sandy "God, how nice ..."
    sandy "I'm going to cum soon...!"
    image sandy_5_28 ='images/characters/sandy/sandy_5/sandy_5_28.jpg'
    scene sandy_5_28
    sandy "Go on ..."
    image sandy_5_29 = Movie(play="images/characters/sandy/sandy_5/sandy_5_29.webm")
    scene sandy_5_29 with fade
    pause(10)
    sandy "Mmm ..."
    image sandy_5_30 ='images/characters/sandy/sandy_5/sandy_5_30.jpg'
    scene sandy_5_30
    sandy "Ahhh, oh my God, how nice."
    image sandy_5_31 ='images/characters/sandy/sandy_5/sandy_5_31.jpg'
    scene sandy_5_31
    sandy "I'm trembling all over, just how I like it..."
    j "(She seems to have just came.)"
    image sandy_5_32 ='images/characters/sandy/sandy_5/sandy_5_32.jpg'
    scene sandy_5_32
    sandy "(Aw what the hell now I have to disinfect it!)"
    j "(Damn it, I did not expect such actions from her, especially since she is so close.)"
    image sandy_5_33 ='images/characters/sandy/sandy_5/sandy_5_33.jpg'
    scene sandy_5_33
    sandy "I, as always, always fall for me."
    image sandy_5_34 ='images/characters/sandy/sandy_5/sandy_5_34.jpg'
    scene sandy_5_34
    sandy "Go to your mistress, you did a good job today."
    image sandy_5_35 ='images/characters/sandy/sandy_5/sandy_5_35.jpg'
    scene sandy_5_35
    sandy "(What's that sticking out from behind the bed?)"
    image sandy_5_36 ='images/characters/sandy/sandy_5/sandy_5_36.jpg'
    scene sandy_5_36
    sandy "Oops."
    sandy "(It's someone's leg!)"
    sandy "(Someone is in my room.)"
    image sandy_5_37 ='images/characters/sandy/sandy_5/sandy_5_37.jpg'
    scene sandy_5_37
    sandy "(Looks like [j]'s boot, is it under my bed?)"
    sandy "(Stop, it can't be.)"
    sandy "I'm probably going insane or I have been fantasizing too much."
    sandy "For what its worth, I should tell him my feelings..."
    sandy "I'll go take another shower and think about what I saw."
    scene black
    pause(1)
    centered "A couple of hours later"
    scene black

    $ renpy.end_replay()
    $ hide_interface = False
    $ sandy_5_comp = True
    $ inventory.drop_task(task_find_phone_pass)
    jump label_sandy_room
    return
