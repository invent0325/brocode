import string

s = "The quick brown fox jumped over the lazy dog!"
print( string.capwords( s ) )
print( s.upper() )
print( s.lower() )
print( s.split() )
print( s.find( "dog" ) )
print(s.casefold())
print(s.replace("dog", "cat"))
print(s.strip("The"))
print(s.endswith("!"))
print(s.startswith("The"))
print(s.islower())