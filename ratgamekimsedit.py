#The game of the Rat
print "     The \n Game of the \n     Rat"
raw_input("Press enter to continue")
print "Choose your character:"
raw_input()
#Drawing character choices
print "Elfred Ratskill"
print "	 	   	          _..----.._      _"
print "	      			.\'  .--.    \"-.(0)_"
print "                  '-.__.-''''=:|   ,  _)_ \__  . c\\'-.."
print "	     			 '''------'---''---'-\""
# enter story here
ratskill_story = {
	"start": {
		"text": "Hello Elfred",
		"choices": []
	}
}
raw_input("...")
print "Sir. Ratsalot"
print "	             (\,/)"
print "                     oo   '''//,        _"
print "                   ,/_;~,        \,    / '"
print "                    \"'  \    (    \    !"
print "                         ',|  \    |__.'"
print "                         '~  '~----''"
# enter story here
ratsalot_story = {
	"start": {
		"text": "Hey Sir Ratsalot...nice to see you again.",
		"choices": []
	}
}
raw_input("...")
print "Ratzo"
print "                .---."
print "           (\./)     \.......- "
print "           >' '<  (__.'\"\"\"\" "
print "          \" ` \" \""
# enter story here
ratzo_story = {
	"start": {
		"text": "...and suddenly a voice\n" +
				"Hi Ratzo...Would you like the package you left me back?\n",
		"choices": {
			"y": ("Yes of course!", "got packet"), # enter this to choose this option: (text, next kex)
			"n": ("No, thanks.", "no packet")
		}
	},
	"got packet": {
		"text": "A package slides out of the darkness towards your bed",
		"choices": []
	},
	"no packet": {
		"text": "\"Very well then, I'll keep it\", \n says the voice\n" +
				"You get out of bed and begin wandering into the darkness\n" +
				"You feel around the room helplessly and touch what feels like a door knob\n",
		"choices": []
	}
}
# bring it all together
all_stories = {
	"Sir. Ratsalot": ratsalot_story,
	"Elfred Ratskill": ratskill_story,
	"Ratzo": ratzo_story
}
#taking character input
#and checking to see if character was typed correctly
character = ""
while True:
	character = raw_input("Which character do you choose?\n-> " )	
	if character in ["Sir. Ratsalot" , "Ratzo" , "Elfred Ratskill"]:
		print "Good choice %s is a great rat" % character
		break	
	else:
		print "You probably mistyped something, let's try entering the rat's name again"
def tell_story(story, key="start"):
	while True:
		obj = story[key]
		print(obj["text"])
		if len(obj["choices"]) == 0:
			# end story if no more options available
			break
		for w in obj["choices"].keys():
			print("%s (%s)" % (obj["choices"][w][0], w))
		answ = raw_input("Enter your choice\n-> ")
		key = obj["choices"][answ][1]
		print "Next key: ", key
print "Let's begin our adventure!"
raw_input("...")
print "You awake in a small ratbed with a candle precariously burning beside the bed."
print "The rest of the room is dark besides the sphere of light around you from the candle."
print "You probably fell asleep reading"
raw_input("...")
print "Thank god you didn't burn the rathouse down."
tell_story(all_stories[character])
