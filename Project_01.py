#Project 01 
## Given dictionary
import random
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
## solve
# use question to get user's tastes (multiple value)
# match randomly with ingredient

def ask_user():
    taste=[]
    for x,y in questions.items():
        print(y)
        ans=input('Please enter YES (Y) or No (N): ')
        if ans== 'Y':
            taste.append(x)
        elif ans== "N":
            continue
        else:
            print ("Error in answer, Exit !:")
            exit
    return(taste)
def return_ing(taste):
    ans=[]
    for j in ingredients.keys():
        if j in taste:
            ans.append(ingredients.get(j)[random.randint(0,2)])
    return (ans)
def print_out(taste,ans):
    print('Tastes you chose: ',taste)
    print('Ingredient added: ',ans)
    return()
# main 
# not sure this is what the Project ask by using def 
Input=ask_user() # ask all questions
Ans=return_ing(Input)
print_out(Input,Ans)
