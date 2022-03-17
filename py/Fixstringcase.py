'''
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
'''
#BDD 
#able to count the case letters
#Able to convert string to lower case
#able to convert  given string t o upper case
#able to covert the srting to lowercase if the uppercase letters are the equal to lowers case letters


#pseudocode
 #initialize cases count to 0
 #loop thru chars counting the number of letter in lowers cases/uppercses
 #if upper is equall to lower or lower is > upper return string to lower 
 #else return string to upper
 #exit
  

def solve(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
    
print(solve('MajeKew'))
print(solve('codejDKELSD'))