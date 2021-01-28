#-----------------------------Suspic---------------------------------------------
label suspic_man:
    call interface from _call_interface_24
    $ renpy.block_rollback()
    image suspic_1_1 ='images/characters/suspic/suspic_1_1.jpg'
    scene suspic_1_1
    j "Hi, do you have something to sell?"
    if suspic_1_comp == False:
        image suspic_1_2 ='images/characters/suspic/suspic_1_2.jpg'
        scene suspic_1_2
        man "Man, fuck off, I don’t know anything."
        image suspic_2_3 ='images/characters/suspic/suspic_2_3.jpg'
        scene suspic_2_3
        j "(I either made a mistake or forgot something.)"
        j "([frank] spoke about the password, but what was it... I think I wrote it down in my notebook...)"
        j "Listen, I know the password:"
        menu:
            "Dirty parrots":
                $ renpy.block_rollback()
                image suspic_3_1 ='images/characters/suspic/suspic_3_1.jpg'
                scene suspic_3_1
                jump suspic_exit
            "Net hares":
                $ renpy.block_rollback()
                image suspic_3_1 ='images/characters/suspic/suspic_3_1.jpg'
                scene suspic_3_1
                jump suspic_exit
            "Dirty teddy bears":
                $ renpy.block_rollback()
                image suspic_3_3 ='images/characters/suspic/suspic_3_3.jpg'
                scene suspic_3_3
                man "Why didn't you just immediately say the password, we just wasted time."
                j "Yes, to be honest, I forgot."
                man "It's okay, what interests you."
                image suspic_2_1 ='images/characters/suspic/suspic_2_1.jpg'
                scene suspic_2_1
                j "I know what school you went to, I need a key to it."
                man "Many people have come to buy all sorts of things from me, but this is a first."
                image suspic_4_1 ='images/characters/suspic/suspic_4_1.jpg'
                scene suspic_4_1
                man "Okay, I have one and that, it will cost you $ 100."
                image suspic_2_2 ='images/characters/suspic/suspic_2_2.jpg'
                scene suspic_2_2
                menu:
                    "{color=#4fb100}Buy a key{/color} -$[school_key.cost]":
                        if inventory.money>= school_key.cost:
                            $ inventory.buy(school_key)
                            $ new_item = True
                            image suspic_4_5 ='images/characters/suspic/suspic_4_5.jpg'
                            scene suspic_4_5
                            man "It was nice dealing with you. Do you want to take a look at the rest of my goods?"
                            j "Alright I'll take a look."
                            $ inventory.drop_task(task_find_suspic)
                            $ inventory.add_task(task_steal_answer_1)
                            $ suspic_1_comp = True
                            $ new_task = True
                            call suspic_shop from _call_suspic_shop
                        else:
                            j "I don't have enough money."
                            image suspic_4_5 ='images/characters/suspic/suspic_4_5.jpg'
                            scene suspic_4_5
                            man "Come when you do have the money."
                            jump suspic_exit
                    "To leave":
                        image suspic_3_1 ='images/characters/suspic/suspic_3_1.jpg'
                        scene suspic_3_1
                        jump suspic_exit
            "Clean rabbits":
                $ renpy.block_rollback()
                image suspic_3_1 ='images/characters/suspic/suspic_3_1.jpg'
                scene suspic_3_1
                jump suspic_exit
    else:
        image suspic_3_3 ='images/characters/suspic/suspic_3_3.jpg'
        scene suspic_3_3
        man "Hi, look what I have for you today."
        jump suspic_shop

label suspic_exit:
    $ hide_interface = True
    call interface from _call_interface_25
    image suspic_3_1 ='images/characters/suspic/suspic_3_1.jpg'
    scene suspic_3_1
    j "(It seems he is leaving.)"
    image suspic_3_2 ='images/characters/suspic/suspic_3_2.jpg'
    scene suspic_3_2
    pause(1)
    $ hide_interface = False
    $ renpy.block_rollback()
    $ suspic_gone = True
    jump park

label suspic_shop:
    $ hide_interface = False
    call interface from _call_interface_26
    image suspic_5 ='images/characters/suspic/suspic_5.jpg'
    scene suspic_5
    menu:
        "Buy 1 picklock - $[picklock.cost]. Amount:[picklock_amount]":
            if inventory.money >=picklock.cost:
                if not picklock in inventory.items:
                    $ inventory.buy(picklock)
                    $ picklock_amount +=1
                    $ new_item = True
                    jump suspic_shop
                else:
                    $ inventory.drop_money(picklock.cost)
                    $ picklock_amount +=1
                    jump suspic_shop
            else:
                j "I don't have enough money."
                jump suspic_shop
        "{color=#6f6c70}Buy sleeping pills. (Available soon){/color}":
            jump suspic_shop
        "{color=#6f6c70}Buy XXX pills. (Available soon){/color}":
            jump suspic_shop
        "Cancel":
            jump suspic_exit
    scene suspic_4_5
