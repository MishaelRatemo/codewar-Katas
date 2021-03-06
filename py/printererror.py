'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
'''
#BDD
# anaylize the error 
# return an error in a fraction of the 
#Pesuodcode
#>>>initialize the errors
#>>> fint the length of the string
#>> loop tthough the string given
#>> test if the letters in the string are going beyond thelast letter and do an increament of the errors found
#>>  then convert the errors in a string 
#>> and the count into a string 
#>> return a fraction to represent the error rate

def printer_error(s):
    errors = 0
    count = len(s)
    for lett in s:
        if lett > "m":
            errors += 1
    return str(errors) + "/" + str(count)

