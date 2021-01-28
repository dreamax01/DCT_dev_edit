#-----------------------------Megan---------------------------------------------
label ASH_1:
    call interface from _call_interface_16
    if day_time == 5:
        image ASH_1_20 ='images/hospital/main/ASH/ASH_1-20.jpg'
        scene ASH_1_20
        j "(Wow, she has very pretty legs.)"
        image ASH_1 ='images/hospital/main/ASH/ASH_1.jpg'
        scene ASH_1 with fade
    else:
        image ASH_1 ='images/hospital/main/ASH/ASH_1.jpg'
        scene ASH_1
    ashley "Hello, did you want something?"
    j "Hello, just passing by..."
    image ASH_2 ='images/hospital/main/ASH/ASH_2.jpg'
    scene ASH_2 with dissolve
    pause (1)
    image ASH_4 ='images/hospital/main/ASH/ASH_4.jpg'
    scene ASH_4 with dissolve
    ashley "Maybe something is bothering you?"
    j "Yes i need sex"
    scene ASH_1 with dissolve
    ashley "Well then come in future versions"
    $ hide_interface = False
    $ ASH_1 = True
    jump hospital_main
    return
