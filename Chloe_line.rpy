#-----------------------------Chloe---------------------------------------------
label chloe_0_1:
    call interface from _call_interface_8
    show school_exit_idle
    pause (0.01)
    image chloe_0_1_1 = "images/characters/chloe/chloe_0_1/chloe_0_1_1.jpg"
    scene chloe_0_1_1 with fade
    j "(So, here comes the time to complete the first task of this bitch.)"
    image chloe_0_1_2 = "images/characters/chloe/chloe_0_1/chloe_0_1_2.jpg"
    scene chloe_0_1_2
    j "([chloe] goes to the toilet.)"
    j "(I have to go after her.)"
    j "(But no one should notice me.)"
    if not renpy.variant("pc") or mini_games_skip:
        jump chloe_r_0_1
    image chloe_0_1_3 = "images/characters/chloe/chloe_0_1/chloe_0_1_3.jpg"
    scene chloe_0_1_3
    $ renpy.pause(0.5, hard='True')
    show prompt_qte:
        yalign 0.5
        xalign 0.5
    with dissolve
    $ renpy.pause(1.0, hard='True')
    pause(3)
    hide prompt_qte with dissolve
    $ renpy.block_rollback()
    $ res = renpy.call_screen("scr_qte", time=2.0, length=2, _layer="master")
    if res:
        $ renpy.block_rollback()
        image chloe_0_1_6 = "images/characters/chloe/chloe_0_1/chloe_0_1_6.jpg"
        scene chloe_0_1_6
        j "Well, it seems like no one noticed me."
    else:
        $ renpy.block_rollback()
        image chloe_0_1_4 = "images/characters/chloe/chloe_0_1/chloe_0_1_4.jpg"
        scene chloe_0_1_4 with dissolve
        centered "{size=72}Have you noticed!"
        image chloe_0_1_5 = "images/characters/chloe/chloe_0_1/chloe_0_1_5.jpg"
        scene chloe_0_1_5 with fade
        girl "Hey, where are you going, men have their own toilet."
        j "I thought something and mixed up a bit."
        girl "Here the tablet is hanging, idiot."
        j "Oh you are right! I must have mistaken!"
        $ hide_interface = False
        jump school_exit
    image chloe_0_1_7 = "images/characters/chloe/chloe_0_1/chloe_0_1_7.jpg"
    scene chloe_0_1_7
    j "I didn't think anyone else would be here."
    j "I've got to hurry, otherwise I will get found out!"
    scene chloe_0_1_7
    $ renpy.block_rollback()
    $ qte_word = qte_word + renpy.random.choice(abc)
    $ res = renpy.call_screen("scr_qte", time=1.5, length=2, _layer="master")
    if res:
        $ renpy.block_rollback()
        image chloe_0_1_8 = "images/characters/chloe/chloe_0_1/chloe_0_1_8.jpg"
        scene chloe_0_1_8
        $ renpy.pause(1.0, hard='True')
        image chloe_0_1_10 = "images/characters/chloe/chloe_0_1/chloe_0_1_10.jpg"
        scene chloe_0_1_10 with fade
        j "(That was easier than I thought.)"
        jump chloe_r_0_1
    else:
        $ renpy.block_rollback()
        centered "{size=72}Have you noticed!"
        image chloe_0_1_9 = "images/characters/chloe/chloe_0_1/chloe_0_1_9.jpg"
        scene chloe_0_1_9 with fade
        girl "What are you doing here?"
        j "Isn't this the Men's toilet?"
        girl "No, fool, this is a toilet for women."
        j "Oh you are right! I must have mistaken!"
        $ hide_interface = False
        jump school_exit
label chloe_r_0_1:
    image chloe_0_1_11 = "images/characters/chloe/chloe_0_1/chloe_0_1_11.jpg"
    scene chloe_0_1_11 with fade
    j "(I think I made it just in time.)"
    j "(This is a pretty fun task after all.)"
    image chloe_0_1_12 = "images/characters/chloe/chloe_0_1/chloe_0_1_12.jpg"
    scene chloe_0_1_12
    j "(I've always longed to know what color her panties were.)"
    image chloe_0_1_13 = "images/characters/chloe/chloe_0_1/chloe_0_1_13.jpg"
    scene chloe_0_1_13
    j "(Oh my god, this is such a good angle!)"
    image chloe_0_1_14 = "images/characters/chloe/chloe_0_1/chloe_0_1_14.jpg"
    scene chloe_0_1_14
    j "(So what color is her underwear...)"
    j "(A couple more successful shots.)"
    image chloe_0_1_15 = "images/characters/chloe/chloe_0_1/chloe_0_1_15.jpg"
    scene chloe_0_1_15
    j "(Oh yeah. Such a photo should go into my personal collection.)"
    image chloe_0_1_16 = "images/characters/chloe/chloe_0_1/chloe_0_1_16.jpg"
    scene chloe_0_1_16
    j "(Alright, [lara] should like these photos.)"
    image chloe_0_1_17 = "images/characters/chloe/chloe_0_1/chloe_0_1_17.jpg"
    scene chloe_0_1_17
    j "(My collection is forming back, now with an addition of these erotic pictures. Excellent!)"
    image chloe_0_1_18 = "images/characters/chloe/chloe_0_1/chloe_0_1_18.jpg"
    scene chloe_0_1_18
    j "(Now I'll have to go meet that bitch.)"
    image chloe_0_1_19 = "images/characters/chloe/chloe_0_1/chloe_0_1_19.jpg"
    scene chloe_0_1_19
    j "(Now I will have something to masturbate to in the Evenings!)"
    scene chloe_0_1_19
    $ renpy.end_replay()
    $ hide_interface = False
    $ CG_25_unlock = True
    $ chloe_0_1_comp = True
    $ inventory.drop_task(task_lara_photo_chloe)
    $ inventory.add_task(task_show_photo_lara)
    $ new_task = True
    jump school_exit
    return
