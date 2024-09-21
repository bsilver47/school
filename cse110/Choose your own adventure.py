#funtion used to ensure that all input integers are valid options
#def good_option(option_val):
    #check if given variable is within proper range
    #if (option_val < 1) or (option_val > 3):
        #while (option_val < 1) or (option_val > 3):
            #print('Hmm, something doesn\'t seem right.')
            #option_val = int(input('What numerical value did you mean to say? (1 or 2)  '))

#main()
#intro
print(f'Welcome Adventurer!')
name = input('May I ask, what is your name?  ')
print(f'It is a genuine pleasure to meet you, {name}!')
name = name.title()
print(f'Now, you are probably wondering why you are unable to see me, correct?')
print('Well, if you recall, three days ago, a missile came and decimated our')
print('entire power grid leaving us unable to get in contact with anyone that is outside')
print('of our dwelling.  Until you awoke, I was the only one able to either take care of')
print('the rest of those still unwell or leave and try to get help.')
print(f'Well, I believe the legends of your heroics do precede you, {name}!')
print('Are all of the stories true? Are you the type that would always leave in')
print('the hope of saving everyone? Will you help our society regain power and help millions?')
option1 = input('Yes/No?  ').lower()

#remainder
if option1.find('yes') != -1:
    print(f'Good show! I knew we could count on you {name}!!  Now, which item will you pick for your protection as you journey to the power plant?')
    option2 = int(input('<Do you choose the (1) broad sword or (2) the nightstick?> (Single number value, please.)  '))
    #option2 = good_option(option2)

    if option2 == 1:
        print(f'I love the Broad Sword! Good choice!  ')
    elif option2 == 2:
        print(f'How courageous choosing the Night Stick!  Noble choice!  ')
    else:
        print('<As you walk up to the table to get a feel for your options, you bump into a chair.>')
        print('<This causes you to think.  You pick up the chair and break it apart.>')
        print('<You now have four chair legs strapped to your back.>')
        print('How clever, this would not have occurred to me...')
    
    print('Well, I suppose there is nothing else to say but to bid farewell and best travels!')
    print('<At that, you walk outside.>')
    print('<Upon walking outside, you are immediately struck by what you see...or should I say, don\'t see.>')
    print('<Even the sky is black.  The world around you is so black that you cannot so much as see your own hand in front of your face.>')
    print('<Yet, seeing as the task needs completed, you set off on your adventure.>')
    print('<Upon walking for a while, you suddenly realize that you have no directions for where you are going.>')
    print('<At the same moment that you come to this realization, you realize that you hear something:  a moaning.>')
    print('<Immediately, you recognize that, with the missile strike that you were informed of, the radiation must have turned this person into a zombie.>')

    if option2 == 1:
        print('<You immediately draw your sword, swinging it about.>')
        print('<Upon feeling your blade connect with your target, you hear a sudden "Ow!" followed by the dull thud of your victim.>')
        print('<You find it odd that this zombie was so refined in his reaction to coming in contact with your blade, but shrug it off justifying that tv couldn\'t have gotten everything right about zombies.>')
        print('<You go to sheath your sword but notice that it is sticky from its most recent use.>')
        print('<Not wanting to ruin the scabbard of this gift, you opt to merely carry it in hand until you can clean it.>')
        print('<So, you merely carry on.>')
    elif option2 == 2:
        print('<You immediately draw your nightstick.>')
        print('<At this particularly unfortunate time, you realize that you\'ve never actually used a nightstick...>')
        print('<So, naturally, you do your best to mimic the only movie in which you can recall someone using a nightstick...or, rather, maglight.>')
        print('<So, copying moves you\'ve only ever seen on Night at the Museum, you start waving around your nightstick, feeling relief in the fact that, if you can\'t see anyone, surely the opposite is true.>')
        print('<Upon connecting, however, you hear a loud "Ow!" followed by the dull thud of your victim falling to the ground.>')
        print('<Your relief from having been victorious quickly dissipates when you hear "What was that for?">')
        print('<Helping your assault victim return to his feet, you apologize and explain that, upon hearing his moaning, you assumed that he was a zombie.>')
        print('<Fortunately, he is quick to forgive and says "Well you clearly couldn\'t have seen me so I suppose it would be vain for me to get angry.">')
        print('<Assuming he is referring to the fact that everything is black, you thank him for his graciousness.>')
        print('<With this out of the way, he offers directions, apologizing that he can\'t take you to where you are going.>')
        print('<You thank him again for how helpful and gracious he has been and set off again, this time with the confidence of going the right direction.>')
    else:
        print('<You immediately draw one of the chair legs and start waving it around, looking for the proper victim to stab.>')
        print('<As you feel it hit someone, you suddenly hear laughing.>')
        print('<Disconcerted, you hesitate.>')
        print('<As you do, you hear a friendly voice ask, "Isn\'t that stick supposed to be, on the ground in front of you, helping you not hit things and people?">')
        print('<Apologizing, you reference that you were on your way to the power plant.>')
        print('<This time it was the victim\'s turn to apologize that he couldn\'take you there himself as he is already so late, but he offers very good directions for you to get there.>')
        print('<You thank him for his help and graciousness and set about on your way, with confidence that you are going the right way.>')
    
    print('<After walking for a while, you recognize the distinct roar of a black bear, mere feet from you.>')
    option4 = int(input('Do you choose to (1) fight or (2) run?  '))#or (3) freeze and get a ride
    #option4 = good_option(option4)

    if option4 == 1:
        if option2 == 1:
            print('<Fortunately, you still have your sword out.>')
            print('<You swing your sword at the bear.>')
            print('<It sticks to the bear.>')
            print('<When you pry off your sword, you expect to hear a roar.>')
            print('<You are then suprised to hear the bear, not roar, but sniff.>')
            print('<You follow suit.>')
            print('<Your heart sinks.>')
            print('<This is not blood.>')
            print('<This is honey.>')
            print('<You did not kill a zombie.>')
            print('<You assaulted an innocent bystandar.>')
            print('<And ruined their groceries.>')
            print('<With the bear distracted with the majority of the honey that was on your sword, you continue on your way.>')

            print('<Stumbling further along your way, you suddenly find that you\'ve set foot into water.>')
            print('<As you do, you suddenly hear someone cry out.>')
            option5 = int(input('<Do you decide to (1) help the distressed soul, or (2) continue on your way?>'))

            if option5 == 1:
                print('<Beginning to seek out the misterious cry for help, you stumble across a small figure.>')
                print('<Very small.>')
                print('<Upon inquiring, you learn that this poor soul is stuck.>')
                print('<Opting to free it, you suddenly hear a great flapping whiz past your head.>')
                print('<Moments later, you hear a new voice.>')
                print(f'Thank you, young {name}.')
                print('You have saved my daughter.')
                print('Naturally, being a fae, I can see into the depths of your mind and understand the turmoil you have been through.')
                print('As a thank you for saving my daughter, I would like to alleviate some of this pain.')
                print('<You can suddenly see everything.>')
                print('<As your vision comes back, you realize a few things at once:>')
                print('<(1) There was never a missile>')
                print('<(2) The person you spoke to at the beginning of this adventure is just crazy>')
                print('<(3) This means that you left several ill people (assuming they exist) in the hands of a mad man)>')
                print('<(4)  The real reason that you couldn\'t see anything (and still can\'t) has nothing to do with being "blind" and everything to with the fact that this is a text based rpg>')
                print(f'Thank you {name} for playing this game, we look forward to working with you again.')
                #end of this storyline
            else:
                print('<Continuing to walk, you suddenly notice a frantic voice coming from next to you, looking for something>')
                print('<As if catching up with an old friend, you start to trivially refer to that stuggling voice you heard before>')
                print('<As if responding to you, you suddenly feel yourself dragged to the ground, unconscious>')
                #end of this storyline
        elif option2 == 2:
            print('<You clumsily hit the bear with your night stick.>')
            print('<Upon making contact, you recognize that you made a mistake.>')
            print('<The bear suddenly swats at your nightstick with a roar.>')
            print('<With that, you\'ve lost your nightstick, but with the bear as angry as it is, you leave it be>')
            print('<So, you limp away as quickly as you can to find safety>')
        else:
            print('<In a surprisingly short battle, after drawing two chair legs, you defeat the bear.>')
            print('<You keep walking, more comfortable with your new pelt draped over your shoulders, confident that you are going the right way from the directions you received.>')
    elif option4 == 2:
        if option2 == 1:
            print('<You decide to start running.>')
            print('<Unfortunately, you still have your sword in hand, still slippery from before.>')
            print('<Your sword slips free from your hand.>')
            print('<Realizing that you do not have time enough to bend down and pick up your sword, you continue running.>')
            print('<The fallen blade holds the bears attention as you run towards safety.>')
            print('<Rather, you run further away from the bear...you\'re still lost and still can\'t see, and now, you do not have your source of defense.>')
        elif option2 == 2:
            print('<As you start to run, you toe comes in contact with a rock.>')
            print('<With a sore toe, you pick up the rock and throw it at the bear.>')
            print('<Obviously this did not hurt the bear much, but it startled the bear enough that you safely got away.>')
            print('<Following the directions that you\'ve received, you find that you safely arrive at your journey\'s destination to sort everything out.>')
        else:
            print('<As you start to run, you draw one chair leg to throw at the bear.>')
            print('<Obviously this did not hurt the bear much, but it startled the bear enough that you safely got away.>')
    else:
        print('<You hesitate.>')
        print('<You hear a gun shot.>')
        print('<The bear falls.>')
        print('<The bear\'s head takes you down with it and rests, lifelessly, on you.>')
        #person feels guilty (explaining bear was sick, they are a ranger) and takes you to the power plant by truck



else:
    print('Very well, I will leave these people to your trusty care and will be sure to return as soon as I can get everything back up and running!')
    print('<You here the sound of him walking toward what must be a table, where he grabs something that sounds long, metallic and sharp.  You then hear him walk out the door.>')
    print('<You now recognize that you are alone.  What do you decide to do next?>')
    option3 = int(input('<Do you choose to (1) find food or (2) check the others?>  '))
    #or (3) nap and wake up to a nurse tending care of you
    #option3 = good_option(option3)

    if option3 == 1:
        print('<You stumble around the dark until you find the kitchen.>')
        print('<Upon discovering the fridge, you find yourself confused by the fact that the fridge is actually cold.>')
        print('<As you make this discovery, you hear footsteps coming up behind you.>')
        option6 = int(input('<Do you decide to (1) attack the approaching person or (2) wait?>'))

        if option6 == 1:
            print('<The invader falls to the ground and, relieved, you sit down to a nice sandwich from the fridge.>')
        elif option6 == 2:
            print('<As you wait and listen, the approaching person suddenly calls you by name:>')
            print(f'{name}! It\'s so great to see you out of bed!  I\'m the nurse that has been tending to you in this mental hospital.')
            print('<You hear the nurse mutter something about finding the schizophrenic patient that has gone missing>')
    elif option3 == 2:
        print('<You stumble around the dark until you find an unconscious body.>')
        print('<As your hand finds a person, there just remains one question: >')
        option7 = int(input('Will you wake them up?  [(1) Yes or (2) No]'))
        if option7 == 1:
            print('<Upon waking them up and talking to the person, they inform you that you are actually in a care facility.>')
            print('<Apparently, being blind, you didn\'t notice the dog that was hang gliding toward you.>')
            print('<This would not have been a problem had the dog been any breed other than the Great Dane that it was.>')
            print('<This dog collided with your head and gave you a concussion, with amnesia and short-term memory loss.>')
        else:
            print('<Upon reaching into the pocket of the unconscious person, you find a sharpie.>')
            print('<After drawing on their face for a while, this individual starts to wake up.>')
            print('<As a result, you quickly get up and run for the door.>')
            print('<Unfortunately, you still can\'t see, so you run into the wall, knocking yourself out.>')
    else:
        print('<You stumble around the dark until you find a bedroom to take a nap.>')
        print('<You awaken to find that there is someone actually now tending to you!>')
    #Player will encounter 3 main trials. Possibly: health related patient, zombie related from outside, zombie infected patient, priority sorting in face of new catastrophy
