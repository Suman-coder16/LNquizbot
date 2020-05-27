#Open a file
question = open("/home/kilanko/LNQuizBot/texts/lnquiz_questions.txt", "r")
fo = list(question)
print (fo)
Mylist = iter(fo)
print (next(Mylist))
