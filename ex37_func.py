# Symbol Review


print "This will print out a 'plain english' definition for all"
print "keywords, data types, string escape sequences, string formats,"
print " and operators of the Python language"
print ""
print ""
print "Sections: \n Keywords \n Data types \n String escape sequences"
print " String formats \n Operators"



def keywords():  
		print section #error check
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
				print "elif Keywords reached"
				break
	
def escapes():
		print section
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
	print section
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
	print section
	#taking user input to decide which section to enter
	section = raw_input("Which section would you like definitions from? \n > ")
	
	if 'keywords' in section and section != 'none':
		keywords()			
	
	elif 'data' or 'types' in section and section != 'none':
		data_types()
		
	elif 'string' or 'escape' in section and section != 'none':
		escapes()
		
	else:
		print "Invalid section typed try again or exit"
		
	
	#asking if programme should start from the beginning 
	section = 'none'
	restart = raw_input("Choose a new section? (y/n) \n > ")
		