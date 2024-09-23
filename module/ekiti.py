from random import choice

capital = "Ado-ekiti"

bird = "pigeon"

flower = "Hibscus"

song = "Ekiti kete"

def randomfunfact():
    funfacts = [
	    "Ado-Ekiti is a city filled with hills and mountains.",
	    "There are various hills, and it is important.",
	    "There are various undulating landscapes there."
    ]
	
    index = choice("0123")

    print(funfacts[int(index)])