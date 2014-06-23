#At point in game where user deciding whether or not to eat contents of box which they
#found out contains peanut butter and oreos.
#want to know if they want to eat peanut butter or oreos, not eat any
# eat just the peanut butter, eat just the oreos, or eat both. 

def string_intersect(input):
	
##Lists for checking against
	O = ["eat", "it"]
	a = ["peanut", "peanut butter"]
	b = ["oreo", "oreos"]
	c = ["peanut", "peanut butter", "oreos", "oreo"]
	d = ["don't", "do not", "not"] # negatives 
	e = ["or", "nor"] # joining



##Checking intersections
	o_o = list(set(O)) & set(input.split())
	a_a = list(set(a) & set(input.split()))
	b_b = list(set(b) & set(input.split()))
	c_c = list(set(c) & set(input.split()))
	d_d = list(set(d) & set(input.split()))
	e_e = list(set(e) & set(input.split()))
	
##Using combinations of intersections to discern meaning

	#If no specifics about which to eat are given
	if len(o_o) >= 1 and len(d_d) = 0 and len(c_c) = 0:
		print "Eat what? The box? Let's not talk like apes"
		#ask for input again
		decision = "confused"
		
	#Trying to figure out what to do if both oreo and peanut included in input
	elif len(c_c) > len(b_b) and len(c_c) > len(a_a): #if 
		print "included peanut and oreo in input"
		
		#list of negatives not empty but two weren't used and no joining words used
		#implying input is using both items but wants opposite actions attached to each
		if len(d_d) != 0 and len(d_d) < 2 and len(e_e) == 0:
			print "eating only one of them"
			#if distance between peanut or peanut butter and *NEGATIVE*	in input.split() greater
			#than distance between oreos and negative than: print "eating peanut butter"
			# but not eating oreos. else: eating peanut butter and not eating oreos.
		
		elif len(d_d) == 1 and len(e_e) != 0:
			print "Not eating either"
			decision = "neither"
		
		#This probably won't be reached unless trying to input something confusing
		elif len(d_d) >= 2:
			print "That's a confusing way to say you are not eating either of them"
			decision = "neither"
		else:
			print "eating both"
			decision = "both"