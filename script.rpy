# Declare characters used by this game.
define r = Character(_("Rajesh"), color="#2cb02c")
define s = Character(_("Suresh"), color="#2121d0")
define a = Character(_("Boy1"), color="#ff9627")
define b = Character(_("boy2"), color="#faf600")
define t = Character(_("teacher"), color="#ff0000")

default knowledge = 1
default charm = 2
default guts = 3
default kindness = 4
default proficiency = 5

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    ##play music "robot.mp3"

    scene bg boarding school
    with fade
    show screen gameUI

    "Today is the first day of Rajesh in his new boarding school."
    #show rajesh at topleft

    "But Rajesh is not happy because it's his first time living away from his parents."

    hide screen gameUI 

    scene bg classroom1
    pause 2.0
    scene bg classroom2
    #show rajesh at top
    with dissolve

    
    "Rajesh in his classroom."

    "Since Rajesh joined the school in middle of the session therefore he was feeling alone and alienated."

    scene bg classroom3

    "Where as on the other hand , children of his class were already divided into groups."

    "So now it was quite difficult for him to make new friends ." 

    scene bg canteen with dissolve
    pause 4.0

    #show rajesh at topleft
    #with fade

    " It was lunch time, the bell ring and all the students were now moving towards the canteen."

    scene bg line
    with fade

    show suresh at topright 
    show rajesh at topleft 
    s "Hey, are you the new admission."

    r "Yes.."
 
    s "I am Suresh."

    r "Hi Suresh! My name is Rajesh"

    s "Nice name , come on now let's stand in the line."

    hide rajesh 
    hide suresh 


    #show boy1 
    scene bg fourboys 
    with fade

    "Rajesh and Suresh  are standing in line suddenly three boys come and stand in front of Rajesh cutting the line."
    scene bg line
    show rajesh at topleft

    r "Hey can you please go and stand at the back instead of cutting the line."

    hide rajesh
    show boy1 at topright

    "Boy turn back and looks at Rajesh and asks"

    a "Hey you are the newbie right?"

    show rajesh at topleft

    r "Yes."

    a "Just stand quietly or I'll knock your brains out."

    hide boy1
    show suresh at topright

    s "Why did you tell them you are newly admitted, come on, let's ask them to leave the line."


    
    menu:

        "Try to convince Suresh since  it's your first day, therefore you don't want to create any problem.":
           
            jump first

        "Agree with Suresh and try to manhandle these boys.":
            
            jump second

        "Try to calm down Suresh and go complain to the teacher.":

            jump third


            


label first:

    hide suresh

    show rajesh at topleft 

    r "No don't . let's leave it because I don't want to ruin my first day otherwise I would have taught them some manners"

    show boy1 at right 

    a "What did you just say that you would have taught me?"

    r "Manners I was talking about manners."

    a "Hmm I see   , what's your room number ?" 

    r "712"

    "Later that day."

    #scene bg basketball #Rajesh walking in badminton court in the evening after school
    #with fade

    #"Kamlesh who is roommate of Rajesh comes and asks Rajesh to come along with him to the room because someone wants to talk to Rajesh"

    #"Rajesh and goes along with Kamlesh to 2 his room."

    scene bg room

    "Rajesh enters the hallway and saw the boys from the canteen along with other two boys standing in the hallway"

    show boy2 at left
    with dissolve
    show boy1 at right
    with dissolve

    

    b "Stands up and asks Rajesh, what were you going to teach us in the canteen?"

    a "From what I can recall, I think it was something about manners"

    b "come on I want to learn some manners show me how will you teach me, come on show me!!!"


    "Others Started cornering him" 

    "They started verbally abusing him"


    menu:

        "try to leave the place and go to a teacher or go to some person who is in authority":
            jump correct

        "try to retaliate verbally and ask them to leave the room.":
            jump neutral

        "try to man handle them and make them leave the room":
            jump incorrect


label second:      

    "{b}Bad Ending{/b}"      
    "I regret to inform you that the option you have chosen may not be the most suitable one. According to the Indian Penal Code, if a child engages in physical aggression towards another child or attempts to harm them, they may be charged under Section 351 of the IPC, which deals with assault and bodily harm. In cases where the child involved is below the age of 18, the Juvenile Justice (Care and Protection of Children) Act 2015 comes into effect." 

    jump Ending


label third:

    r "Hey it's okay instead of going to them let's go and complain to the teacher"

    scene bg canteen

    "Rajesh goes and complains to the teacher standing in the canteen"

    show rajesh at topleft

    r "Sir, these boys are trying to bully us They came and forcefully stood in front of  us in the line and they are not budging even after I requested them to join the line at the back."

    show teacher at topright

    t "Is that so ? let me check"

    hide rajesh
    hide teacher

    "Rajesh and teacher go towards the boys"

    show teacher at top

    t "Am i hearing right ? are you boys trying to bully the new admission ? dont you know how to stand in a queue?"


    a "No sir no !we didn't cut the line."

    r "No sir they did cut the line they came and stood in front of us."
    
    s "Yes sir they did cut the line."

    t "You three go and stand at the back of the line."

    scene bg basketball  
    
    "Rajesh goes to badminton court and after sometime Kamlesh ask him to come to the room"
    
    scene bg room

    "Kamlesh who is roommate of Rajesh comes and asks Rajesh to come along with him to the room because someone wants to talk to Rajesh"

    "Rajesh and goes along with Kamlesh to 2 his room."

    "Rajesh enter the room and seas the boys from the canteen along with other two boys are sitting in his room"

    show boy2 at left
    with dissolve
    show boy1 at right
    with dissolve


    b "Already acting like a teacher's pet huh? Trying to act all smart"

    r "What do you mean ? I did what was necessary you guys were trying to cut the line" 

    a "This pet talks too much let's teach him to stay quiet."

    

    menu:

        "try to leave the place and go to the teacher or go to someone who is in auhority":
            jump correct

        "try to retaliate verbally and ask them to leave the room.":
            jump neutral

        "try to manhandle them and make them leave the room":
            jump incorrect


label correct: 

    scene black

    "{b}Correct choice{/b}"


    "Hey Rajesh"
    "You've made the right choice by opting to leave the premises and seek assistance from a person in authority. In the event that the children attempting to intimidate you continue their behavior, they can be charged under Section 506, which pertains to the punishment for criminal intimidation according to the Indian Penal Code. Furthermore, if these children are below the age of 18, the Juvenile Justice (Care and Protection) Act 2015 will come into effect."

    jump Ending

label neutral: 

    scene black

    "{b}not bad but can be better{/b}"

    "Hey Rajesh"
    "Verbal retaliation may not be the most prudent course of action, as it appears that their intention is not to reach a resolution but rather to intimidate you. Engaging in such behavior could lead to potential charges under Section 506 of the Indian Penal Code, which deals with punishment for criminal intimidation. It's worth noting that if the individuals involved are below the age of 18, the Juvenile Justice (Care and Protection) Act 2015 would be applicable."

    jump Ending


label incorrect:

    scene black

    "{b}Bad Ending{/b}"
    "Hey Rajesh"
    "I regret to inform you that the option you have chosen may not be the most suitable one. According to the Indian Penal Code, if a child engages in physical aggression towards another child or attempts to harm them, they may be charged under Section 351 of the IPC, which deals with assault and bodily harm. In cases where the child involved is below the age of 18, the Juvenile Justice (Care and Protection of Children) Act 2015 comes into effect."

    jump Ending


label Ending:

    return