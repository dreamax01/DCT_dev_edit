#-----------------------------Lara---------------------------------------------
label lara_1:
    call interface from _call_interface_48
    if lara_1_comp == False:
        show gg_hall_idle
        pause (0.01)
        image lara_1_1 = "images/characters/lara/lara_1/lara_1_1.jpg"
        scene lara_1_1 with fade
        j "Hi, are you okay ?!"
        image lara_1_promo = "images/characters/lara/lara_1/lara_1_promo.jpg"
        scene lara_1_promo:
            zoom 1
            xanchor 0 yanchor 0 xpos 0 ypos -2700
        with dissolve
        scene lara_1_promo:
            zoom 1
            xanchor 0 yanchor 0 xpos 0 ypos -2700
            linear 8.0 xpos 0 ypos 0
        $ renpy.pause(7.0, hard='True')
        lara "Oh god you scared me."
        lara "My name is [lara], I'm your housekeeper."
        lara "Are you [j]?"
        image lara_1_5 = "images/characters/lara/lara_1/lara_1_5.jpg"
        scene lara_1_5
        j "Yes that's right."
        j "Sorry to scare you, wasn't on purpose."
        image lara_1_2 = "images/characters/lara/lara_1/lara_1_2.jpg"
        scene lara_1_2
        lara "I am very glad to meet you."
        lara "I will drop by your place sometimes to do the chores."
        j "But everything was covered in dust..."
        image lara_1_3 = "images/characters/lara/lara_1/lara_1_3.jpg"
        scene lara_1_3
        lara "Yes, I noticed. But don't worry I'll clean it up!"
        image lara_1_7 = "images/characters/lara/lara_1/lara_1_7.jpg"
        scene lara_1_7
        j "By the way, is that your bike in the garage?"
        image lara_1_4 = "images/characters/lara/lara_1/lara_1_4.jpg"
        scene lara_1_4
        lara "Yeah, does it bother you?"
        j "No, not at all, on the contary, it's a very interesting model!"
        j "I just wanted to tell you."
        j "If you need any help, you can contact me."
        image lara_1_8 = "images/characters/lara/lara_1/lara_1_8.jpg"
        scene lara_1_8
        lara "Well I'll keep that in mind!"
        image lara_1_6 = "images/characters/lara/lara_1/lara_1_6.jpg"
        scene lara_1_6
        lara "By the way, I actually do have a request and since you suggested..."
        j "I'm all ears."
        j "(This might help me learn about her.)"
        lara "I'm running out of a special cleaning agent."
        lara "And I don't have time to drop by the store."
        lara "Could you help me get it?"
        scene lara_1_5
        j "Of course I will!"
        scene lara_1_3
        lara "Thank you! You really helped me out."
        image lara_1_9 = "images/characters/lara/lara_1/lara_1_9.jpg"
        scene lara_1_9
        lara "I'll give you my number, so be sure to contact me if you have any questions."
        j "Great! Got it!"
        $ lara_1_comp = True
        $ inventory.add_task(task_buy_detergent)
        $ new_task = True
    image lara_1_2 = "images/characters/lara/lara_1/lara_1_2.jpg"
    scene lara_1_2
    lara "Thank you, and to be honest, I'm still very busy! Can you not distract me anymore."
    j "I understand how I get the cleaning product, I’ll bring it right away."
    scene lara_1_2
    $ hide_interface = False
    $ renpy.block_rollback()
    jump label_hall_room
    return

label lara_2:
    call interface from _call_interface_49
    show gg_living_room_idle
    image lara_2_1_1 = "images/characters/lara/lara_2/lara_2_1_1.jpg"
    scene lara_2_1_1 with fade
    lara "Oh, you came."
    image lara_2_1_2 = "images/characters/lara/lara_2/lara_2_1_2.jpg"
    scene lara_2_1_2 with dissolve
    lara "Did you get the detergent?"
    image lara_2_2_1 = "images/characters/lara/lara_2/lara_2_2_1.jpg"
    scene lara_2_2_1
    j "Yes, here you go."
    image lara_2_5_2 = "images/characters/lara/lara_2/lara_2_5_2.jpg"
    scene lara_2_5_2
    lara "Well, now I can wipe away all the stains, including from the carpet in the living room."
    lara "I don’t know what you ate here, but the spots are white and dried."
    image lara_2_6_1 = "images/characters/lara/lara_2/lara_2_6_1.jpg"
    scene lara_2_6_1
    lara "The carpet will be like new."
    image lara_2_7_1 = "images/characters/lara/lara_2/lara_2_7_1.jpg"
    scene lara_2_7_1
    lara "Thank you, you really helped out."
    j "Well if you need anything else, just contact me!"
    image lara_2_3_1 = "images/characters/lara/lara_2/lara_2_3_1.jpg"
    scene lara_2_3_1
    lara "Okay."
    image lara_2_3_2 = "images/characters/lara/lara_2/lara_2_3_2.jpg"
    scene lara_2_3_2 with dissolve
    lara "Maybe we could take a walk in the park after I'm done with work. I wanted to talk to you about something."
    image lara_2_4_1 = "images/characters/lara/lara_2/lara_2_4_1.jpg"
    scene lara_2_4_1
    j "Yes of course!"
    j "See you in the evening!"
    scene lara_2_3_1
    lara "See you."

    $ hide_interface = False
    $ lara_2_comp = True
    $ inventory.drop(detergent)
    $ inventory.drop_task(task_buy_detergent)
    $ inventory.add_task(task_meet_lara_park)
    $ new_task = True
    jump label_living_room
    return

label lara_3:
    call interface from _call_interface_50
    show park_idle
    image lara_3_1_1 = "images/characters/lara/lara_3/lara_3_1_1.jpg"
    scene lara_3_1_1 with fade
    j "Hi, I didn’t know that you smoke."
    image lara_3_1_2 = "images/characters/lara/lara_3/lara_3_1_2.jpg"
    scene lara_3_1_2 with dissolve
    lara "Haha, hello."
    image lara_3_1_3 = "images/characters/lara/lara_3/lara_3_1_3.jpg"
    scene lara_3_1_3
    lara "That's not the only thing you'll find out now, sit down."
    image lara_3_2_2 = "images/characters/lara/lara_3/lara_3_2_2.jpg"
    scene lara_3_2_2
    j "Well, what is it, tell me."
    image lara_3_2_1 = "images/characters/lara/lara_3/lara_3_2_1.jpg"
    scene lara_3_2_1
    lara "You know, I recently cleaned your room and found something amazing."
    image lara_3_2_3 = "images/characters/lara/lara_3/lara_3_2_3.jpg"
    scene lara_3_2_3
    lara "This is a collection of photos of your naked girlfriends."
    image lara_3_3_1 = "images/characters/lara/lara_3/lara_3_3_1.jpg"
    scene lara_3_3_1
    lara "There's [megan] and everyone else, I don't know where you got it from, but I definitely found a treasure for myself."
    image lara_3_3_2 = "images/characters/lara/lara_3/lara_3_3_2.jpg"
    scene lara_3_3_2
    lara "And you know, I figured out how to use them to my advantage."
    lara "I took them and you'll have to get them back."
    image lara_3_3_4 = "images/characters/lara/lara_3/lara_3_3_4.jpg"
    scene lara_3_3_4
    lara "I mean you don't want the pictures to get to the respective owners right, I don't think you can even look them in the eye after that..."
    lara "Nothing personal, it's just business."
    image lara_3_3_5 = "images/characters/lara/lara_3/lara_3_3_5.jpg"
    scene lara_3_3_5
    j "Well you seem like a really cute girl, but in actuality you're such a bitch!"
    image lara_3_3_6 = "images/characters/lara/lara_3/lara_3_3_6.jpg"
    scene lara_3_3_6
    lara "You are also very kind, and while you were looking for a detergent, I found something more interesting."
    scene lara_3_3_1
    lara "I have 5 tasks I need you to complete, and for completing each of them, I'll return you one photo and you can continue to masturbate to them."
    scene lara_3_3_6
    j "(She got me in her trap...)"
    j "And what if I go to the police?"
    scene lara_3_3_2
    lara "You can try, but you can't prove anything."
    lara "In any case, these photos will be with your roommates."
    lara "Therefore I suggest you don't try anything funny."
    image lara_3_3_3 = "images/characters/lara/lara_3/lara_3_3_3.jpg"
    scene lara_3_3_3
    lara "And so, your first assignment."
    lara "You know your foreign language teacher, [chloe]? Take a picture of her ass."
    lara "And I don't mean the erotic pictures from your collection, I need indecent ones."
    lara "Pictures in which she doesn't even know she's being photographed, such as when she's in the toilet."
    scene lara_3_3_1
    lara "Do it and I'll return you one of your photographs."
    scene lara_3_3_2
    lara "Honest exchange."
    scene lara_3_3_6
    j "And how will I know that you are not deceiving me."
    image lara_3_3_7 = "images/characters/lara/lara_3/lara_3_3_7.jpg"
    scene lara_3_3_7
    lara "Is this evidence not enough for you?"
    image lara_3_3_8 = "images/characters/lara/lara_3/lara_3_3_8.jpg"
    scene lara_3_3_8
    lara "Don't worry, this is just a copy. I'm not stupid enough to bring the original."
    image lara_3_3_9 = "images/characters/lara/lara_3/lara_3_3_9.jpg"
    scene lara_3_3_9
    j "You are fucking blackmailing me!"
    scene lara_3_3_4
    lara "I'll say it again, it's nothing personal. Just doing business."
    image lara_3_4_1 = "images/characters/lara/lara_3/lara_3_4_1.jpg"
    scene lara_3_4_1
    lara "If you complete this task, you will receive the following."
    image lara_3_5_1 = "images/characters/lara/lara_3/lara_3_5_1.jpg"
    scene lara_3_5_1
    lara "Good luck, loser."
    image lara_3_6_1 = "images/characters/lara/lara_3/lara_3_6_1.jpg"
    scene lara_3_6_1
    j "I have to come up with something."
    j "Probably have to do these stupid tasks."
    scene park_idle

    $ hide_interface = False
    $ lara_3_comp = True
    $ inventory.drop_task(task_meet_lara_park)
    $ inventory.add_task(task_lara_photo_chloe)
    $ new_task = True
    jump park
    return

label lara_4:
    call interface from _call_interface_51
    show gg_jack_room_idle
    image lara_4_1 = "images/characters/lara/lara_4/lara_4_1.jpg"
    scene lara_4_1 with fade
    j "Can you stop cleaning my room?"
    image lara_4_2 = "images/characters/lara/lara_4/lara_4_2.jpg"
    scene lara_4_2
    lara "And why is that? Afraid I'll find something else?"
    j "That too, I just don't want to see you."
    image lara_4_4 = "images/characters/lara/lara_4/lara_4_4.jpg"
    scene lara_4_4
    lara "But you have to, you don’t want everyone to know your secret, little pervert."
    image lara_4_5 = "images/characters/lara/lara_4/lara_4_5.jpg"
    scene lara_4_5
    lara "Okay, I was joking."
    lara "Have you brought anything for me?"
    image lara_4_3 = "images/characters/lara/lara_4/lara_4_3.jpg"
    scene lara_4_3
    j "Yes, give me the photo."
    image lara_4_8 = "images/characters/lara/lara_4/lara_4_8.jpg"
    scene lara_4_8
    lara "No matter how patient you are, you will get your picture, first show me the result of your work."
    image lara_4_9 = "images/characters/lara/lara_4/lara_4_9.jpg"
    scene lara_4_9
    j "Admire."
    image lara_4_10 = "images/characters/lara/lara_4/lara_4_10.jpg"
    scene lara_4_10
    lara "Wow! But for it to be from such an angle... You really took the photos well."
    image lara_4_6 = "images/characters/lara/lara_4/lara_4_6.jpg"
    scene lara_4_6
    lara "You're a big lad. I told you it's not difficult and you did it."
    image lara_4_7 = "images/characters/lara/lara_4/lara_4_7.jpg"
    scene lara_4_7
    j "It wasn't that easy, actually."
    image lara_4_13 = "images/characters/lara/lara_4/lara_4_13.jpg"
    scene lara_4_13
    lara "I think you have a real talent for creating such photos."
    lara "I can see that this is one of your first works, but still a commendable effort."
    image lara_4_14 = "images/characters/lara/lara_4/lara_4_14.jpg"
    scene lara_4_14
    j "Don't flatter me."
    j "I want to get these photos back and have nothing to do with you anymore."
    image lara_4_15 = "images/characters/lara/lara_4/lara_4_15.jpg"
    scene lara_4_15
    lara "There is a time for everything, asshole."
    lara "In the meantime, close the door and listen to the next assignment."
    image lara_4_17 = "images/characters/lara/lara_4/lara_4_17.jpg"
    scene lara_4_17
    lara "You know that I wash your clothes and see everything that you wear."
    lara "But I don't see any of [megan]'s sexy underwear"
    image lara_4_18 = "images/characters/lara/lara_4/lara_4_18.jpg"
    scene lara_4_18
    lara "As far as I know, she washes those herself so no one sees it."
    lara "Bring those to me, and we'll see which one of us looks better on it."
    image lara_4_16 = "images/characters/lara/lara_4/lara_4_18.jpg"
    scene lara_4_16
    j "You've got to be kidding me. I don't even know where I can get her underwear and besides, she's bound to notice her underwear going missing."
    image lara_4_20 = "images/characters/lara/lara_4/lara_4_20.jpg"
    scene lara_4_20
    lara "Well, to be honest, those are your problems not mine."
    lara "I don’t care how you do it, but bring me this underwear."
    scene lara_4_6
    lara "Don't worry, you'll get to see me in it and judge for yourself how I look in it, and when that time comes you can finally masturbate to me."
    image lara_4_19 = "images/characters/lara/lara_4/lara_4_19.jpg"
    scene lara_4_19
    j "God, I thought that I was a pervert but it turns out that you were the one."
    image lara_4_20 = "images/characters/lara/lara_4/lara_4_20.jpg"
    scene lara_4_20
    lara "Everyone has their own fetishes, we live in a modern and tolerant world."
    image lara_4_21 = "images/characters/lara/lara_4/lara_4_21.jpg"
    scene lara_4_21
    lara "Good luck again."
    j "Yeah."
    image lara_4_22 = "images/characters/lara/lara_4/lara_4_22.jpg"
    scene lara_4_22
    j "Bitch!"
    lara "I will pretend that I did not hear this."
    scene lara_4_21
    pause(1)

    $ hide_interface = False
    $ lara_4_comp = True
    $ inventory.drop_task(task_show_photo_lara)
    $ inventory.add_task(task_steal_meg_underwear)
    $ CG_26_unlock = True
    $ new_task = True
    jump label_jack_room
    return

label lara_5:
    call interface from _call_interface_52
    show gg_garage_room_idle
    image lara_5_1 = "images/characters/lara/lara_5/lara_5_1.jpg"
    scene lara_5_1 with fade
    lara "Well hello."
    lara "Do you have any news for me?"
    image lara_5_4_0 = "images/characters/lara/lara_5/lara_5_4_0.jpg"
    image lara_5_4_1 = "images/characters/lara/lara_5/lara_5_4_1.jpg"
    if megan_status == "House":
        scene lara_5_4_0
    else:
        scene lara_5_4_1
    j "(I would have never thought that such a nice looking girl can be such a bitch.)"
    image lara_5_8 = "images/characters/lara/lara_5/lara_5_8.jpg"
    scene lara_5_8
    j "It was not easy."
    image lara_5_10_0 = "images/characters/lara/lara_5/lara_5_10_0.jpg"
    image lara_5_10_1 = "images/characters/lara/lara_5/lara_5_10_1.jpg"
    if megan_status == "House":
        scene lara_5_10_0
    else:
        scene lara_5_10_1
    j "Will this suit you?"
    image lara_5_9 = "images/characters/lara/lara_5/lara_5_9.jpg"
    scene lara_5_9
    lara "Wow! This is just what I needed!"
    j "What do I do if she starts looking for them?"
    image lara_5_5 = "images/characters/lara/lara_5/lara_5_5.jpg"
    scene lara_5_5
    lara "Don't worry, I'll return it to her soon, she wouldn't even notice that it was gone."
    image lara_5_6 = "images/characters/lara/lara_5/lara_5_6.jpg"
    scene lara_5_6
    lara "First I’ll put it on and then bring it back."
    scene lara_5_8
    lara "So you don't have to worry."
    lara "You'll receive your photo very soon, just that I don't have it  with me right now."
    image lara_5_7_0 = "images/characters/lara/lara_5/lara_5_7_0.jpg"
    image lara_5_7_1 = "images/characters/lara/lara_5/lara_5_7_1.jpg"
    if megan_status == "House":
        scene lara_5_7_0
    else:
        scene lara_5_7_1
    j "And what if you're lying to me?"
    image lara_5_2 = "images/characters/lara/lara_5/lara_5_2.jpg"
    scene lara_5_2
    lara "Well you don't have a choice so you just have to take my word for it."
    image lara_5_3 = "images/characters/lara/lara_5/lara_5_3.jpg"
    scene lara_5_3
    lara "You will get it soon."
    image lara_5_7_0 = "images/characters/lara/lara_5/lara_5_7_0.jpg"
    image lara_5_7_1 = "images/characters/lara/lara_5/lara_5_7_1.jpg"
    if megan_status == "House":
        scene lara_5_7_0
    else:
        scene lara_5_7_1
    j "Somehow it just sounds fishy."
    image lara_5_12 = "images/characters/lara/lara_5/lara_5_12.jpg"
    scene lara_5_12
    lara "Ha ha ha"
    image lara_5_11 = "images/characters/lara/lara_5/lara_5_11.jpg"
    scene lara_5_11
    lara "See you."

    scene lara_5_11
    $ hide_interface = False
    $ lara_5_comp = True
    $ inventory.drop_task(task_steal_meg_underwear)
    $ inventory.drop(sexy_ling_megan)
    jump label_garage
    return

label lara_6:
    $ hide_interface = True
    call interface from _call_interface_53
    image lara_6_1 = "images/characters/lara/lara_6/lara_6_1.jpg"
    scene lara_6_1
    j "Zzz... Zzz... Zzz..."
    lara "(Oh, look who's still sleeping.)"
    lara "(Maybe it's time to wake him up?)"
    image lara_6_2 = "images/characters/lara/lara_6/lara_6_2.jpg"
    scene lara_6_2
    lara "(He sleeps so sweetly, I won’t wake him up.)"
    lara "(Probably too tired from doing my tasks.)"
    image lara_6_3 = "images/characters/lara/lara_6/lara_6_3.jpg"
    scene lara_6_3
    lara "(This is a good moment to take a closer look at him.)"
    lara "(If my rustling from coming into the room did not wake him up, he sure sleeps like a log.)"
    lara "(We must take advantage of this!)"
    image lara_6_4 = "images/characters/lara/lara_6/lara_6_4.jpg"
    scene lara_6_4
    lara "(He sure is a sweetheart!)"
    lara "(Will I ever have the chance...)"
    image lara_6_5 = "images/characters/lara/lara_6/lara_6_5.jpg"
    scene lara_6_5
    lara "(I never thought I would be interested in this bastard.)"
    image lara_6_6 = "images/characters/lara/lara_6/lara_6_6.jpg"
    scene lara_6_6
    lara "(I wonder what is hidden under his covers ?!)"
    image lara_6_7 = "images/characters/lara/lara_6/lara_6_7.jpg"
    scene lara_6_7
    lara "(Wow! Look at how sexy he is in his boxers.)"
    lara "(I definitely looked here for a reason.)"
    lara "(Phew, it's really getting hot in here.)"
    lara "(I'm really getting hot, I should take off my cardigan.)"
    image lara_6_8 = "images/characters/lara/lara_6/lara_6_8.jpg"
    scene lara_6_8
    lara "(Yes, that’s much better.)"
    image lara_6_9 = "images/characters/lara/lara_6/lara_6_9.jpg"
    scene lara_6_9
    lara "(Mmm, how I miss the male body.)"
    image lara_6_11 = "images/characters/lara/lara_6/lara_6_11.jpg"
    scene lara_6_11
    lara "(It seems like he's not waking up anytime soon.)"
    image lara_6_12 = "images/characters/lara/lara_6/lara_6_12.jpg"
    scene lara_6_12
    lara "(Well, it's early in the morning but it seems like something else has woken up. I could have some fun with this.)"
    image lara_6_13 = "images/characters/lara/lara_6/lara_6_13.jpg"
    scene lara_6_13
    lara "(And he wouldn't even notice anything.)"
    image lara_6_14 = "images/characters/lara/lara_6/lara_6_14.jpg"
    scene lara_6_14
    lara "(This is much easier, I think he would have liked it if he had seen me.)"
    image lara_6_14 = "images/characters/lara/lara_6/lara_6_14.jpg"
    scene lara_6_14
    lara "(Mmm, it's so hard to resist.)"
    lara "(I think he would have liked me.)"
    image lara_6_15 = "images/characters/lara/lara_6/lara_6_15.jpg"
    scene lara_6_15
    lara "(I'm going to help myself to it for a little while and he wouldn't even realise it.)"
    image lara_6_16 = "images/characters/lara/lara_6/lara_6_16.jpg"
    scene lara_6_16
    lara "(Come here, boy, help me relax.)"
    image lara_6_17 = "images/characters/lara/lara_6/lara_6_17.jpg"
    scene lara_6_17
    lara "(Yes, I can feel his hot penis, even through his clothes.)"
    lara "(And he has a great penis.)"
    lara "(Mmm ...)"
    image lara_6_18 = Movie(play="images/characters/lara/lara_6/lara_6_18.webm")
    scene lara_6_18 with dissolve
    pause(10)
    lara "(Oh my god, how nice.)"
    lara "(This is better than vibrators.)"
    lara "(And I am in full control.)"
    image lara_6_19 = "images/characters/lara/lara_6/lara_6_19.jpg"
    scene lara_6_19
    lara "(You are beautiful, [j].)"
    lara "(It's such a pity that you're asleep.)"
    lara "(Let's see what's down below.)"
    lara "(A little more and he will tear these underpants and burst out.)"
    lara "(And I will not stop it.)"
    image lara_6_20 = "images/characters/lara/lara_6/lara_6_20.jpg"
    scene lara_6_20 with fade
    lara "(Yes, that’s much better.)"
    lara "(God, look at how big he is!)"
    image lara_6_22_0 = "images/characters/lara/lara_6/lara_6_22_0.jpg"
    scene lara_6_22_0
    lara "(I'm going to help myself to it!)"
    image lara_6_22 = Movie(play="images/characters/lara/lara_6/lara_6_22.webm")
    scene lara_6_22 with fade
    pause(10)
    lara "(It's so girthy! I can't even grab it completely with my hand!)"
    image lara_6_23_0 = "images/characters/lara/lara_6/lara_6_23_0.jpg"
    scene lara_6_23_0
    lara "(He's definitely blessed!)"
    image lara_6_23 = Movie(play="images/characters/lara/lara_6/lara_6_23.webm")
    scene lara_6_23 with fade
    pause(10)
    lara "(It's been a long time since I've last held a cock in my hand.)"
    image lara_6_24 = "images/characters/lara/lara_6/lara_6_24.jpg"
    scene lara_6_24
    lara "(I wonder how does it taste like.)"
    image lara_6_26_0 = "images/characters/lara/lara_6/lara_6_26_0.jpg"
    scene lara_6_26_0
    lara "(Mmm... it doesn't even fit completely in my mouth...)"
    image lara_6_26 = Movie(play="images/characters/lara/lara_6/lara_6_26.webm")
    scene lara_6_26 with fade
    pause(10)
    lara "(He is so hot but so cute...)"
    image lara_6_27 = "images/characters/lara/lara_6/lara_6_27.jpg"
    scene lara_6_27
    lara "(Perfect cock...)"
    image lara_6_28 = Movie(play="images/characters/lara/lara_6/lara_6_28.webm")
    scene lara_6_28 with fade
    pause(10)
    lara "(He seems to like it.)"
    image lara_6_29 = "images/characters/lara/lara_6/lara_6_29.jpg"
    scene lara_6_29 with flashbulb
    lara "(Oh! So much cum!)"
    lara "(Its been awhile since I last seen cum splurt out like that!)"
    lara "(Cum flowing down his cock, what a beautiful sight.)"
    lara "(I wonder how much sperm is in it.)"
    lara "(He obviously did not jerk off for a long time.)"
    scene lara_6_12
    lara "(He just showed himself perfectly!)"
    lara "(It will be necessary to meet with him later.)"
    image lara_6_30 = "images/characters/lara/lara_6/lara_6_30.jpg"
    scene lara_6_30
    lara "(I almost forgot his photograph.)"
    lara "(So, I'll put it under the pillow!)"
    image lara_6_31 = "images/characters/lara/lara_6/lara_6_31.jpg"
    scene lara_6_31
    lara "(I'm glad I didn't give the original!)"
    lara "(But he doesn't have to know that yet.)"
    image lara_6_32 = "images/characters/lara/lara_6/lara_6_32.jpg"
    scene lara_6_32
    j "What a cool morning, I feel so good."
    scene lara_6_32

    $ renpy.end_replay()
    $ CG_27_unlock = True
    $ hide_interface = False
    $ lara_6_comp = True
    jump label_jack_room
    return
