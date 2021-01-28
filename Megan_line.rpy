#-----------------------------Megan---------------------------------------------
label megan_0_3:
    call interface from _call_interface_56
    $ renpy.block_rollback()
    image megan_0_3_1 ='images/characters/megan/megan_0_3/megan_0_3_1.jpg'
    scene megan_0_3_1
    menu:
        "{color=#4fb100}Start searching{/color}":
            jump megan_r_0_3
        "Cancel":
            $ hide_interface = False
            jump label_megan_room
label megan_r_0_3:
    scene megan_0_3_1
    j "(So, [megan] is not at home right now, which means I can safely search for what I need.)"
    j "(That bitch Lara said to bring her [megan]'s sexy underwear.)"
    j "(But how do I find what I need?)"
    image megan_0_3_2 ='images/characters/megan/megan_0_3/megan_0_3_2.jpg'
    scene megan_0_3_2
    j "(I think we should start with this cabinet..)"
    image megan_0_3_3 ='images/characters/megan/megan_0_3/megan_0_3_3.jpg'
    scene megan_0_3_3
    j "(Going through every little thing, but I did not find anything interesting.)"
    image megan_0_3_4 ='images/characters/megan/megan_0_3/megan_0_3_4.jpg'
    scene megan_0_3_4
    j "(What I need is probably in the next closet.)"
    image megan_0_3_5 ='images/characters/megan/megan_0_3/megan_0_3_5.jpg'
    scene megan_0_3_5
    j "(Oh! Just what I needed!.)"
    image megan_0_3_6 ='images/characters/megan/megan_0_3/megan_0_3_6.jpg'
    scene megan_0_3_6
    j "(I didn’t think it would be so simple.)"
    "The sounds of doors opening could be heard..."
    image megan_0_3_7='images/characters/megan/megan_0_3/megan_0_3_7.jpg'
    scene megan_0_3_7
    j "(Fuck, did [megan] come back earlier.)"
    image megan_0_3_8 ='images/characters/megan/megan_0_3/megan_0_3_8.jpg'
    scene megan_0_3_8
    j "(Damn! I have to do something!)"
    image megan_0_3_9 ='images/characters/megan/megan_0_3/megan_0_3_9.jpg'
    scene megan_0_3_9
    megan "(Damn, I think I forgot my purse in the car.)"
    megan "(I really need a vacation from work.)"
    scene megan_0_3_7
    j "(Hiding in the closet is the only way now!)"
    image megan_0_3_10 ='images/characters/megan/megan_0_3/megan_0_3_10.jpg'
    scene megan_0_3_10 with fade
    megan "God, I'm so tired! It's a good thing that I have a flexible work schedule."
    image megan_0_3_11 ='images/characters/megan/megan_0_3/megan_0_3_11.jpg'
    scene megan_0_3_11
    megan "Now I can relax, finally."
    image megan_0_3_12 ='images/characters/megan/megan_0_3/megan_0_3_12.jpg'
    scene megan_0_3_12
    megan "And how does such a beauty like me not have a man yet."
    image megan_0_3_13 ='images/characters/megan/megan_0_3/megan_0_3_13.jpg'
    scene megan_0_3_13 with fade
    megan "I really miss having men in my life."
    megan "My husband is always on business trips, probably with women."
    image megan_0_3_14 ='images/characters/megan/megan_0_3/megan_0_3_14.jpg'
    scene megan_0_3_14
    megan "And here lies a beauty that is waiting for him. I wish someone could just take me from behind."
    image megan_0_3_15 ='images/characters/megan/megan_0_3/megan_0_3_15.jpg'
    scene megan_0_3_15
    megan "Okay thats enough fantasizing for now."
    megan "But before that, I've got to measure something."
    j "(Oh god it's good that she didn't open my closet door.)"
    image megan_0_3_16 ='images/characters/megan/megan_0_3/megan_0_3_16.jpg'
    scene megan_0_3_16 with fade
    megan "Ah, this dress looks great on me, it's a pity that no one will ever see me in it."
    megan "And for whom do I even keep myself in shape for?!"
    image megan_0_3_17 ='images/characters/megan/megan_0_3/megan_0_3_17.jpg'
    scene megan_0_3_17
    j "She is really hot, I haven't seen her naked in a long time and yet she is still getting prettier and prettier!"
    image megan_0_3_18 ='images/characters/megan/megan_0_3/megan_0_3_18.jpg'
    scene megan_0_3_18 with fade
    megan "I'll just leave it here and wait for the day I can actually wear it for someone."
    image megan_0_3_19 ='images/characters/megan/megan_0_3/megan_0_3_19.jpg'
    scene megan_0_3_19 with fade
    j "(She really does have nice curves!)"
    j "(And I found out where she keeps all her lingerie!)"
    image megan_0_3_20 ='images/characters/megan/megan_0_3/megan_0_3_20.jpg'
    scene megan_0_3_20
    j "(Which is great!)"
    j "Well done, [megan] didn't find me."
    image megan_0_3_21 ='images/characters/megan/megan_0_3/megan_0_3_21.jpg'
    scene megan_0_3_21
    j "(She has no need for it now anyways.)"
    scene megan_0_3_21

    $ renpy.end_replay()
    $ hide_interface = False
    $ megan_0_3_comp = True
    $ megan_status = "House"
    $ inventory.add(sexy_ling_megan)
    $ new_item = True
    jump label_megan_room
    return
