#-----------------------------Frank---------------------------------------------
label frank_at_main:
    call interface from _call_interface_46
    $ renpy.block_rollback()
    image frank_1_1 ='images/characters/frank/frank_1/frank_1_1.jpg'
    scene frank_1_1
    frank "Hi bro. What's up?"
    image frank_1_2 ='images/characters/frank/frank_1/frank_1_2.jpg'
    scene frank_1_2
    if sandy_1_comp == True and frank_1_comp == False:
        j "Hi [frank]. I have a deal for you."
        image frank_1_3 ='images/characters/frank/frank_1/frank_1_3.jpg'
        scene frank_1_3
        frank "Tell me."
        image frank_1_4 ='images/characters/frank/frank_1/frank_1_4.jpg'
        scene frank_1_4
        j "Listen, I desperately need to get here at night, and I can’t think of anything but to fake a key."
        image frank_1_5 ='images/characters/frank/frank_1/frank_1_5.jpg'
        scene frank_1_5
        frank "Hahah, why do you have to sneak in at night? You can already walk around here freely during the day."
        image frank_1_6 ='images/characters/frank/frank_1/frank_1_6.jpg'
        scene frank_1_6
        j "I am aware, but I need it at night."
        j "Will you help me or will you scoff at me?"
        image frank_1_7 ='images/characters/frank/frank_1/frank_1_7.jpg'
        scene frank_1_7
        frank "I will help you just cause we've been long time friends. But on one condition, you will have to tell me why you need it."
        image frank_1_8 ='images/characters/frank/frank_1/frank_1_8.jpg'
        scene frank_1_8
        j "I agree, I will tell you later."
        image frank_1_9 ='images/characters/frank/frank_1/frank_1_9.jpg'
        scene frank_1_9
        frank "I know a guy who studied here a long time ago, and from what I know, he never did graduate."
        frank "Nowadays he does all the shady stuff and he can definitely get you what you need."
        frank "You can meet him in the park at night."
        frank "He is not always there, but quite often."
        frank "But I can't say how much this service would cost."
        frank "He is so suspicious that you will immediately notice him."
        image frank_1_10 ='images/characters/frank/frank_1/frank_1_10.jpg'
        scene frank_1_10
        frank "Say the password: Dirty teddy bears."
        frank "But make no mistake, otherwise you will have to come another day."
        image frank_1_12 ='images/characters/frank/frank_1/frank_1_12.jpg'
        scene frank_1_12
        j "Bro, this is very useful information."
        j "Thank you very much."
        image frank_1_13 ='images/characters/frank/frank_1/frank_1_13.jpg'
        scene frank_1_13
        frank "Yes, not at all, but do you remember about our agreement."
        frank "And that I am very curious."
        j "No problem, after I handled it, I'll tell you everything."
        $ frank_1_comp = True
        $ inventory.drop_task(task_talk_frank)
        $ inventory.add_task(task_find_suspic)
        $ new_task = True
    else:
        j "Hi [frank], I'm a little busy right now."
        frank "No problem, good luck."
    $ hide_interface = False
    $ renpy.block_rollback()
    jump school_main
