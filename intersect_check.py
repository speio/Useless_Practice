#At point in game where user deciding whether or not to eat contents of box which they
#found out contains peanut butter and oreos.
#want to know if they want to eat peanut butter or oreos, not eat any
# eat just the peanut butter, eat just the oreos, or eat both. 

def intersect_check(input):
	
##Lists for checking against
	O = ["eat", "it"]
	a = ["peanut", "peanut butter"]
	b = ["oreo", "oreos"]
	c = ["peanut", "peanut butter", "oreos", "oreo"]
	d = ["don't", "do not", "not"] # negatives 
	e = ["or", "nor"] # joining

	decision = "none"

##Checking intersections
	o_o = list((set(O)) & set(input.split()))
	a_a = list((set(a)) & set(input.split()))
	b_b = list((set(b)) & set(input.split()))
	c_c = list((set(c)) & set(input.split()))
	d_d = list((set(d)) & set(input.split()))
	e_e = list(set(e) & set(input.split()))
	
##Using combinations of intersections to discern meaning
	while decision == "none":
		print "O %s" % o_o
		print "a %s" % a_a
		print "b %s" % b_b
		print "c %s" % c_c
		print "d %s" % d_d
		print "e %s" % e_e 
		input = str(raw_input("(internal)input response to check \n > "))
		
		o_o = list((set(O)) & set(input.split()))
		a_a = list((set(a)) & set(input.split()))
		b_b = list((set(b)) & set(input.split()))
		c_c = list((set(c)) & set(input.split()))
		d_d = list((set(d)) & set(input.split()))
		e_e = list(set(e) & set(input.split()))


		#If no specifics about which to eat are given
		if len(o_o) >= 1 and len(d_d) == 0 and len(c_c) == 0:
			print "Eat what? The box? Let's not talk like apes"
			#ask for input again
			decision = "confused"
			print decision
			
		#If neither food is to be eaten
		elif len(o_o) >= 1 and len(d_d) >= 1:
			print "I guess you're not eating either?"
			decision = "not either"
			print decision	
			
			
		#Trying to figure out what to do if both oreo and peanut included in input		
		elif len(c_c) > len(b_b) and len(c_c) > len(a_a): #if 
			print "included peanut and oreo in input"
		
			#list of negatives not empty but two weren't used and no joining words used
			#implying input is using both items but wants opposite actions attached to each
			if len(d_d) != 0 and len(d_d) < 2 and len(e_e) == 0:
				print "eating only one of them"
				input_list = list(input.split())
				
				#finding the index of the negative
				index = 0
				found = "no"
				while found != "yes":
					index = index + 1
					print index
					if input_list[index] in d:
						print "found index of negative"
						i_negative = index
						found = "yes"
						 
					else:
						print "not found yet"
						
				#finding index of peanut 
				index = 0
				found = "no"
				while found != "yes":
					index = index + 1
					print index
					if input_list[index] in a:
						print "found index of peanut"
						i_peanut = index
						
						#getting distance between peanut and negative
						dist_peanut = i_peanut - i_negative
						found = "yes"
						 
					else:
						print "not found yet"
				
				#finding index of oreos
				index = 0
				found = "no"
				while found != "yes":
					index = index + 1
					print index
					if input_list[index] in b:
						print "found index of oreos"
						i_oreos = index
						
						#getting distance between oreos and negative
						dist_oreos = i_oreos - i_negative
						found = "yes"
						 
					else:
						print "not found yet"	
				
				#negative before object assumption
				if i_negative < i_peanut and i_negative < i_oreos:
					
					if dist_peanut > dist_oreos:
						print "eating peanut butter"
				
					else:
						print "eating oreos"
							
						
				
				#negative after object assumption
				else:
					if dist_peanut > dist_oreos:
						print "eating oreos"
					else:
						print "eating peanut butter"	
					

		
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
				print decision	
		
		#Eating just the penut butter (no mention oreos)
		elif len(o_o) >= 1 and len(a_a) >= 1 and len(b_b) == 0:
			print "eating just the peanut butter \n no mention of oreos"
		
		elif len(o_o) >= 1 and len(b_b) >= 1 and len(a_a) == 0:
			print "eating just oreos, no mention of peanut butter"
		
		else:
			print "Not sure what that means, give it another go"
			decision = "none"

user_input = str(raw_input("input response to check \n > "))
intersect_check(user_input)			
