# Symbol Review

print ""
print ""
print "This will print out a 'plain english' definition for all"
print "keywords, data types, string escape sequences, string formats,"
print "and operators of the Python language"
print ""
print ""


def def_keywords(word):
		if word == 'and':
			print "andstuff"
	
		elif word == 'del':
			print "delstuff"
		
		elif word == 'from':
			print "fromstuff"
	
		else:
			print "Sorry that keyword doesn't seem to exist in the list"
			print "Likely because there are lots of keywords and"
			print "I didn't want to, define them all."
			
def keywords():  
		#will use this variable later to ask to input new keyword in same section		
		cont = 'y' 
		
		while cont == 'y':
			print "Press enter to see all keyword choices, or type a keyword"
		
			see_list = raw_input("> ")
			#creating a boolean variable to decide which nested code block to enter
			list_bool = see_list == '' 
		
			if list_bool == True:
				print "and     del     from     not     while     as     elif"
				print "global     or     with     assert     else     if     pass"
				print "yield     break       except       import       print       class"
				print "exec       in       rais       continue       finally       is       return"
				print "def        for       lambda       try"
		
			elif list_bool == False:
				def_keywords(see_list)
				
				cont = raw_input("Input a new keyword?(y/n) \n > ")
				
def escapes():
		cont = 'y'
		while cont == 'y':
			print "Press enter to see all String Escape Sequences choices,"
			print "or type the String Escape you would like a definition for."
		
			see_list = raw_input("> ")
			list_bool = see_list == '' 
		
			if list_bool == True:
				#opening a file with string escapes because idk how to type them here
				with open('escapes.txt', 'r') as f:
					lineArr = f.read()
					print lineArr #Should probably put a check if file exits here
					
			elif list_bool == False:
				print "elif in string escape reached"
				break
				
def data_types():
	cont = 'y'
	while cont == 'y':
		print "Press enter to see all data types, or type a data type"
	
		see_list = raw_input("> ")
		list_bool = see_list == '' 
	
		if list_bool == True:
			print "True     False     None     Strings     Numbers     Floats"
			print "Lists"
		
		elif list_bool == False:
			print "elif in data types reached"
			break

#defining starting values for some variables
section = 'none'
restart = 'y'


#Starts while loop to allow continuation with new sections if desired
#Based on variable restart
while restart == 'y':
	print "Sections: \n Keywords \n Data types \n String escape sequences"
	print " String formats \n Operators"
	#taking user input to decide which section to enter
	section = raw_input("Which section would you like definitions from? \n > ")
	
	if 'keywords' in section:
		keywords()			
	
	elif 'data' in section or 'types' in section:
		data_types()
		
	elif 'string' in section or 'escape' in section:
		escapes()
		
	else:
		print "Invalid section typed try again or exit"
		
	
	#asking if programme should start from the beginning 
	section = 'none'
	restart = raw_input("Choose a new section? (y/n) \n > ")
		