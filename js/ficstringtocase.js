// #BDD 
// #able to count the case letters
// #Able to convert string to lower case
// #able to convert  given string t o upper case
// #able to covert the srting to lowercase if the uppercase letters are the equal to lowers case letters


// #pseudocode
//  #initialize cases count to 0
//  #loop thru chars counting the number of letter in lowers cases/uppercses
//  #if upper is equall to lower or lower is > upper return string to lower 
//  #else return string to upper
//  #exit
function solve(s){
    var lowercounts= 0;
    var uppercounts=0;

    for(let char=0; char < s.length; char++){
        if(s[char]== s[char].toUpperCase()){
            uppercounts++
        }
        else{
            lowercounts++
        }
    }
    return lowercounts >= uppercounts ? s.toLowerCase() : s.toUpperCase()
}

print(solve('AMkejhsA'))
    