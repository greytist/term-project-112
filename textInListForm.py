#peter with the debugging import W
def createTextList(app):
  Text =\
    [ 
      [
          "this text wont show up hehe",
        ],

      [#1
        "You wake up to the sound of your alarm chirping beside your bed. Today is your first",
        "day of classes as a second year CMU student. You just transfered from some other",
        "school nobody has heard of, so you haven't met anybody yet."
        ],

      [#2
        "Your old friend made a fun harmless bet with you the previous day, that you wouldn't",
        "be able to get a date within 3 days. For some reason, you thought that was a real",
        "possibility and took their bet. Your situation is that you have zero acquaintances,",
        "difficult classes to pass, and a lot to lose. But enough worrying, it's time for",
        "your first day of classes!"
        ],

        [#changeAt3 chaneg to morning
        "You walk across Forbes with a big group of other students. Maybe one of them is in",
        "your first class? Suddenly, someone walking the opposite direction from you bumps",
        "into your shoulder."
        ],

        [#changeAt4 blake enters but we dont know him yet
        """"Hey, watch where you're heading." """
        ],

        [#changeAt5 blake no longer speaking
        "A tall guy dressed in formal attire gives you a mean glance, but he stops in",
        "his tracks after seeing your face."
        ],

        [#changeAt6 blake speak but ???
        """"Wait a minute.. why haven't I met you before? You don't have the overly excited""",
        """look of a freshman but you also don't seem to know where you're going..." """
        ],

        [#7
        """"Aha! You must be a transfer student! Am I right, or am I right?" """
        ],

        [#changeAt8 no talking to
        "You nod your head, having trouble figuring out what could possibly be going on inside",
        "the mind of this overly dressed student."
        ],

        [#changeAt8.1 "???"
        """"What is your name, newbie?" """
        ],

        [""],

        [#changeAt9 set player name also no more Blake
        "The strange guy smirks, reaches into his pocket and hands you a card." 
        ]]
  return Text

def loadRestOfText(app):
  moreText=\
      [  [#changeAt10 WE GOT BLAKE YEAA
         f'"Nice to meet you, {app.playerName}. The name is Blake."',
          f'"Here is my card if you ever need anything."'
        ],

        [#10.1
          ["Nice to meet you",1],
          ["You look weird",0],
          [""""See you around champ (sunglasses emoji)." """],
          [""""Dang, I could say the same for you." """]
        ],

        [#changeAt11 no more Blake :(
        "Blake walks off just in time to catch the walk light, leaving you dumbfounded",
        "and holding a business card. These CMU students are a different breed. You have",
        "no idea how to process the interaction you just had, so you continue your walk to",
        "your next class and hope nothing else like that happens again."
        ],

        [#changeAt12 DOHURTY
        "After walking around in this building for almost 10 minutes, you start to panic.",
        "Where the heck is this classroom? Why are there so many staircases that lead to",
        "the same floor? Where are you? What year is it? That's when a girl walks briskly",
        "past you with a boba in her hand, like she owns the place."
        ],

        [#13
        "You call out a quick excuse me in her direction and she stops and glances back",
        "at you."
        ],

        [#changeAt14 "???"
        """"Hi. Do you need something? Oh, you're looking for the same class as me!""",
        """It's this way, here come on we have two minutes left until lecture starts!" """
        ],

        [#changeAt15 no more Charlie
        "Without checking to make sure you're following, she hops up the stairs and",
        "disappears. This girl is quick! Yet you manage to make it through the doors",
        "after her and sit down somewhere in the middle of the room."
        ],

        [#16
        "The professor looks up from their screen and gathers everyone's attention,",
        "starting class. Your first lecture! How exciting!"
        ],

        [#17 do lecture game
          ""
        ],

        [#18 leave game
        ["Wow that lecture sure was rough. It's only day one but you covered so much",
        "material and were assigned a few homework assignments too! Good thing you",
        "managed to scribble down some notes, you definitely plan on reviewing those",
        "later. Next time you will get the right answer!"],#wrong answer
        ["Wow that lecture sure was rough, but you managed to pull through! Although",
         "you still got tons of homework assigned to you, you had a good time. Make",
          "sure you study! Good job getting the right answer."] #right answer
        ],

        [#18.1
         "You forgot to eat breakfast this morning because of how excited you were,",
         "so you are pretty hungry. You are not really sure if the food is good, but",
         "you have heard about this cafe in the univerity center called Au Bon Pain,",
         "and even though you don't know how to say it, you decide to go anyways."
        ],

        [#18.2
         "On your way to the university center, you spot Blake, the guy in the suit,",
         "going in through the doors. Who knows, maybe you'll see him for lunch."
        ],

        [#18.3
         "You made it to ABP! They have sandwiches and pastries and nice drinks. As",
         "you stand in the long line for sandwiches, Blake walks up to you from the",
         "counter. He just got his order."
        ],

        [#18.4 Blake appears
         f'"Hey {app.playerName}. Fancy seeing you here, I love ABP. I am gonna',
         """go sit over there, come find me when you get your food." """
        ],

        [#18.5 blake leav
         "After ordering your food, waiting for a bit, and waiting for a bit more,",
         "you grab your sandwich, chips, and drink and go find Blake. He is talking to",
         "who you assume are his friends but when he sees you he goes back to where his",
         "stuff is. He has a half eaten sandwich and a bag of BBQ chips." 
        ],

        [#18.6 blakeeee
         f'"Hey {app.playerName}! First taste of Au Bon Pain right? What kind of',
         f'chips did you get? Hope you picked a good one."'
        ],

        [##18.7 OPTIONS!!!
        ["Original",0],
        ["BBQ",1],
        [f'"Ah, just plain. I get it, you do not want to be overwhelmed on your',
         f'first day. No no, I understand."'],
        [f'"You have good taste my friend! We will get along just fine!"']
        ],

        [#18.8
         """"I eat here a lot because it is a lot closer to my next class than my""",
         """actual favorite place, which is Hunan. Gotta love the spicy chicken." """
        ],

        [#18.9
         ["Sounds smart",1],
         ["Sounds lazy",0],
         [f'"{app.playerName}, you catch my vibe so well. We should hang out more."'],
         [f'"{app.playerName}, do you not know that time is money? Never waste time."']
        ],

        [#18.99
         "Woa! Would you look at the time! Your class starts in 9 minutes. You panic",
         "and say goodbye to Blake, then head out back to Doherty."
        ],

        [#19-2
         "Amazingly, your afternoon class happened to be in the same room as your",
         "morning class was so you remembered how to get there and made it on time.",
         "Hopefully you pay attention in this lecture!"  
        ],

        [#19-1 (lecture)
         ""
        ],

        [#19-0 no mor lecture
         ["Yikes, was the professor even speaking english? You didn't catch anything",
          "that they said the whole 80 minutes. Better luck next time."],
          ["Nice job! You are on a roll, look at you smarty pants. This class is going",
          "to be a breeze at this rate. Hopefully it doesn't get any harder.."]
        ],

        [#a
         "Wow, it's been a super long day! You sure are tired. It might be best to go",
         "back to your dorm and study some more, so you decide to head back for the night."
        ],

        [#b meeting charlie
         "On your way across Forbes, you notice the girl from your morning class is going",
         "the same way as you. She happens to feel your eyes on her, and she turns to lock",
         "eyes with you."
        ],

        [#c
         """"Hey there! I remember you from this morning. Sorry I couldn't catch your name.""",
         f'{app.playerName}? What an interesting name."'
        ],

        [#d
         """"...My name? OH! My name is Charlie, it's nice to officially meet you!""",
         """I'll see you tomorrow in class."""
        ],

        [#E choices!!!!
         ["sit with me?",1],
         ["see you later",0],
         [f'"WOA! Take me out to dinner first. Haha, I am just joking. Sure I will sit',
          f'with you, {app.playerName}! Bye, have a nice night."'],
         [f'"Bye, see you tomorrow!"']
        ],

        [#f
         "Once you are back in your room, you eat a hot pocket and study for an hour,",
         "but not before taking a nice hot shower.",
        ],

        [#g (next day button)
          ""
        ],

        [#h
         "ZZZZZZZZZzzzzzzZZZzZZzzZzzzZZZZZZZZZzzzzZZZzzZ honk shoooo honk shoo"
        ],
 
        [#19 good morning!
        "Rise and shine buttercup. You have two days left on your bet! Luckily you met two",
        "silly people yesterday that you think you might have a chance with. Although,",
        "you should make sure to keep your grades up so that you don't end up failing."
        ],

        [#19.1
         "You cross forbes with your bag and empty stomach. Food would be so nice right now",
         "but you can't afford to miss class. You walk into Doherty and that girl Charlie",
         "is just down the hall. You decide to go talk to her."
        ],

        [#19.2
         f'"Good morning, {app.playerName}! I am doing well, thanks. Is it not such a',
         f'beautiful morning today?"'
        ],

        [#19.3
         ["It's raining",0],
         ["Very nice yes",1],
         [""""I was just trying to lighten the mood, no need to shoot me down." """],
         [""""Yay! I'm glad you agree!" """]
        ],

        [#19.4
         "You two walk in together, but it is really crowded so instead of standing around",
         "awkwardly looking for seats, you part ways."
        ],

        [#19.5 lecture!
         ""
        ],

        [#19.6
         ["You're starting to notice a theme of of classes being way too hard. It's like",
          "trying to teach quantum theory to a toddler. Or at least, that's what you told",
          "yourself when you didn't pass the lecture check."],
         ["What a great way to start off the day! This win has given you a morale boost",
          "which gives you the energy to recover from studying so much last night.",
          "Good job!"]
        ],

        [#20
        "After your class, you walk oustide of Doherty with an empty stomach. Learning",
        "is a lot of work! That's when you see Charlie looking all bummed out a couple",
        "steps away. You decide to go see what is bothering her."
        ],

        [#21 sad Charlie
        f'"Oh, hey {app.playerName}.. Oh, I am just a bit bummed out because my friend"',
        """was supposed to come get lunch with me but she is sick. I don't know what""",
        """I should do now.." """
         ],
        
        [#22 no charlie
        "This is a perfect opportunity! Not her being sad, but now she has nobody to eat",
        "lunch with. You ask her if she would join you, since you're both by yourselves."
        ],

        [#23 charlie back still sad tho
        """"With you? Hmm..." """
        ],

        [#24 charlie happy now!
        """"Sure! Okay, that sounds fun. Do you want to go to La Prima? I haven't had my""",
        """coffee yet today." """
        ],

        [#25 no charlie
        "Nice! You're finally making new friends, and who knows, maybe one step closer to",
        "winning that bet you made with you old friends. You walk with Charlie, who is",
        "leading the way since you have never been to La Prima. You two walk down the Mall",
        "towards Wean."
        ],

        [#26 scene to la prima
        'As you walk into this building, you hear a group of freshmen calling it "the turtle",',
        "which you can sort of see, but not really since it's just a building. La Prima is",
        "quite busy, the line is moving slow because of all the freshmen who don't know how to",
        "use their meal blocks."
        ],

        [#27 charlie saad
        """"Oh my gosh! There's so many people here. We will have to wait in this long line,""",
        """is that okay? You don't have any classes soon do you?" """
        ],

        [#28 no charlie
        "You reassure Charlie that the next class you have isn't until a lot later. She",
        "seems to feel a bit better after hearing this."   
        ],

        [#29 charli happy
        """"Okay, great! I would hate for you to not be able to eat lunch! Lets go stand""",
        """in line. So how are you doing today?" """
        ],

        [#30
        "You and Charlie have nice conversations while waiting . After you order,",
        "you two sit in the back where the last two empty seats are. After waiting",
        "a bit longer, you two hear the barista call Charlie's name."
        ],

        [#31 charlie happy
        """"Oh, they just called my name. It's a bit crowded in here, do you mind getting""",
        """my coffee while I go wash my hands? I'll be quick." """
        ],

        [#32 LA PRIMA GAME!!!
        ""
        ],

        [#33! narration 
        "There were so many chairs pushed out into the walkways, you had a rough time",
        "maneuvering through them. Luckily, you make it back to your table just in",
        "time to see Charlie hopping back from the restrooms."
        ],

        [#34 charlie :)
        f'"Thank you so much for getting my coffee for me, {app.playerName}! I',
        """wouldn't want anybody grabbing it by mistake, especially since it is so""",
        """busy right now. Let's eat!" """
        ],

        [#35
        "As you both finish up your small lunch, you think the coffee and muffin you",
        "got were pretty mid. Charlie seemed to really like it though."
        ],

        [#36 ANSWER CHOICES!!
        f'"I feel so much better now, thank you for coming with me {app.playerName}.',
        """What did you think of your first prima coffee?" """
        ],

        [#37 :)) choose ur own responce
        ["It's great",1],
        ["It's just okay",0],
        [""""Yay! Isn't it the best? I love this coffee so much!" """],
        [""""Oh, you don't like it? That's upsetting.." """]
        ],

        [#38
         "You had decided to skip your next lecture while waiting for the coffees, since",
         "they took so long to come out. You figured you can review the lecture slides",
         "later that night before you sleep. But anyways, it is getting late so you say",
         "your goodbyes to Charlie and head back to your dorm."
        ],

        [#39
         "Ahhh.. your dorm is so nice and cozy. Too bad you have to study instead of",
         "relaxing. It's okay, it will pay off later. After you study for an hour, you",
         "shower and then pass out in bed."
        ],

        [#40
          "eep"
        ],

        [#41
         "zzZzZzZZZZzzzzzzZZZZZZzzzzz honk mimimimim honk mimimimi"
        ],

        [#42
         "Good morning sleepyhead! Today you woke up a little extra early to go grab",
         "breakfast. You get out of bed, grab your stuff, and head over to good ole",
         "La Prima in Wean hall."
        ],

        [#43
         "To your surprise, you see Blake finishing up his order at the counter. Usually",
         "you see him walking across Forbes. You go to where he sat down and ask him",
         "what he is doing."
        ],

        [#44
         f'"Hey champ. How are you? Me? I have a very important meeting soon. I need a',
         f'coffee to help wake me up. Oh, sounds like they just called my name. Do you',
         f'mind getting that for me? Thanks chief."'
        ],

        [#45
         ""  
        ],

        [#46
         "You grab Blake's coffee and hand it to him just as he takes off for his",
         "meeting. What a busy guy. You take your own breakfast with you to go, so",
         "that you can make it to class."
        ],

        [#47
         "You eat your croissant on your way to Doherty. By the time you get to lecture,",
         "it's all gone and you sit quietly in your seat waiting for the professor to",
         "start for the day."
        ],
        
        [#48
         "lectreu"
        ],

        [#49
         ["Lecture is starting to become too fast for you, you cannot keep up with the",
         "pace. You can't retain any information! Today's topic slips from your brain."],
         ["Good job! Lots of your classmates missed this one today. Look at you go,",
          "you're so smart! You passed Go, collect 200."]
        ],

        [#end game sequence!!
         "This is the beginning of the end.. let's see who you have managed to rizz."
        ],

        [#the question blush
         "Who are you going to ask out?"
        ],

        [#!!!!
         ["Blake"],
         ["Charlie"],
         ["You remember Blake saying that he would be getting dinner at his second favorite",
          "CMU dining establishment, ABP. You decide to go try your luck with him there."],
         ["Charlie said she likes usually heads back to her dorm around this time, and",
          "she usually studies in Wean where she has easy access to La Prima. You decide",
          "to go intercept her on her way back."]
        ],

        [#no going back
         "This is it. There's no going back now. You take a deep breath as you leave Doherty",
         "to finally ask out your soon-to-be date."
        ]
          ]
  return moreText

def loadFinalScene(app, person):
  if person=="CharlieW":
    return(
    [
    [#1
      "You head towards Wean, and soon enough you run into Charlie on her way back."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to walk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Charlie blushes and her jaw drops in surprise. What will she say?"],
      ["Charlie blushes and her jaw drops in surprise. What will she say?"]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}.. I..."'
    ],

    [#5 ...
     f'"Okay! Sure, why not? I will go on a date with you."'
    ],

    [#6 SUCCESS
     "You did it. You won the bet, AND you get to go on a date now. It's a win/win",
     "scenario. You and Charlie walk back across Forbes and say your goodbyes as you",
     "part ways. The end."
    ]
    ])
  elif person=="CharlieNotLike":
    return(
      [
       [#1
      "You head towards Wean, and soon enough you run into Charlie on her way back."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to walk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Charlie looks pretty surprised, but she squints her eyes in a confused manner.",
       "What will she say?"],
      ["Charlie looks pretty surprised, but she squints her eyes in a confused manner.",
       "What will she say?"]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}.. I..."'
    ],

    [#5
     """"I don't actually like you that much. You're just always around, so I talk to you." """
    ],

    [#6 oh no..
     "WOA that was harsh!!! Hint taken, you leave Charlie alone and go back to your dorm",
     "by yourself. Not only did you lose the bet, but you got ripped up by this girl",
     "you've only known for 3 days. Massive L."
    ]
    ])
  elif person=="CharlieNotSmart":
    return(
      [
       [#1
      "You head towards Wean, and soon enough you run into Charlie on her way back."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to walk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Charlie looks pretty surprised, and she starts laughing. That's weird. What",
       "will she say?"],
      ["Charlie looks pretty surprised, and she starts laughing. That's weird. What",
       "will she say?"]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}.. I..."'
    ],

    [#5
     """"Your grades are way too low, you would just bring me down. Sorry, no."""
    ],

    [#6 oop
     "Wow. That was a lot more direct than she usually is, and to be frank just plain",
     "rude. Are grades really that important.. it's only been 3 days. Either way, you",
     "were rejected and now face the reality of losing the bet, and walking back to your",
     "dorm all sad. Better luck next time."
    ]
    ])
  elif person=="BlakeW":
    return(
    [
    [#1
      "You head towards ABP, and soon enough you spot Blake sitting in the Skibo cafe."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to talk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Blake takes a moment to process your question. After a moment, he smiles. What",
       "will he say?"],
      ["Blake takes a moment to process your question. After a moment, he smiles. What",
       "will he say?"]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}."'
    ],

    [#5
     """"I think that would be beneficial for both of us. Sure, why not?" """
    ],

    [#6 SUCCESS
     "You did it. You won the bet, AND you get to go on a date now. It's a win/win",
     "scenario. Blake suggests going to breakfast, which is great because you don't"
     "normally eat breakfast. You make plans for the next morning and part ways. The End."
    ]
    ])
  elif person=="BlakeNotLike":
    return(
    [
    [#1
      "You head towards ABP, and soon enough you spot Blake sitting in the Skibo cafe."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to talk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Blake laughs at you. Wow this can't be good."],
      ["Blake laughs at you. Wow this can't be good."]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}."'
    ],

    [#5
     """"You're not interesting, I will not waste my time on you. Your opinions suck, too." """
    ],

    [#6
     "!!!!",
     "Wow, why does he even talk to you then, you share no classes together."
    ]
    ])
  elif person=="BlakeNotSmart":
    return(
    [
    [#1
      "You head towards ABP, and soon enough you spot Blake sitting in the Skibo cafe."
      ],

    [#2
     f'"Hi {app.playerName}. What are you doing here? Do you want to talk with me?"'
    ],

    [#3 the question
      ["Will you go on",2],
      ["a date with me?",2],
      ["Blake thinks for a moment, then puts his hands together on the table. What",
       "will he say?"],
      ["Blake thinks for a moment, then puts his hands together on the table. What",
       "will he say?"]
    ],

    [#4 THE RESPONCE!!!
     f'"{app.playerName}."'
    ],

    [#5
     """"It would not be smart of me to even consider that, with grades like yours. No." """
    ],

    [#6 oop
     "Wow. He says what's on his mind a lot, but that was very soul crushing. Are grades",
     "really that important.. it's only been 3 days. Either way, you were rejected and",
     "now face the reality of losing the bet, and walking back to your dorm all sad.",
     "Better luck next time."
    ]
    ])
