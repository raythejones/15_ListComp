#true or false based on if it meets all of the requirements set forth
def isValid(testPass):
    countUpCase = [ x for x in testPass if x.isupper() ]
    countLowCase = [ x for x in testPass if x.islower() ]
    countDigit = [ x for x in testPass if x.isdigit() ]
    if (len(countUpCase) == 0 or len(countLowCase) == 0 or len(countDigit) == 0):
	return False
    else:
        return True
        
print isValid("334") 
#should return false

print isValid("kskskkjjddSSSddsjkjj") 
#should return false

print isValid("sS0") 
#should return true


#strength is based on how many of the different kinds of 
def strength(testPass):
    countUpCase = [ x for x in testPass if x.isupper() ]
    countLowCase = [ x for x in testPass if x.islower() ]
    countDigit = [ x for x in testPass if x.isdigit() ]
    countChar = [ x for x in testPass if not(x.isalnum()) ]
    sum = 2 * len(countUpCase) + len(countLowCase) + 2 * len(countDigit) + 3 * len(countChar)
    rating = sum / 2
#if it exceeds 10, just return 10 since that's the highest on the scale
    if rating > 10:
        return 10
    return rating

print strength("a")
# should return 0

print strength("ooSP33.?")
# should return 8 