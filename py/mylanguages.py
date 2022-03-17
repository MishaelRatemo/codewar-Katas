'''
You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.

Note: the scores will always be unique (so no duplicate values)

Examples
{"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
'''


results={"Java": 10, "Ruby": 80, "Python": 65}   

def my_languages(results):
    # BDD
    #>> should be abe able to retun a list of languages test score
    #>> The test score should be equal to 60 or greater than 60
    #>> the returned array should be in descensing order
    
    # Pseudocodes
    # >> sort the the given arrary
    #>> loop though the array
    #>> check if the items meet the criteria
    return sorted((lang for lang,result in results.items() if result>=60), reverse=True, key=results.get)


print(my_languages(results))