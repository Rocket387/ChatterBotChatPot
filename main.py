from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #train the chatbot using ListTrainer
from ChatCleaner import clean_corpus

#creates an instance of ChatBot
chatbot = ChatBot("Chatpot")
CORPUS_FILE = "chat.txt"

#passing the chatbot to ListTrainer
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

#conversation samples that’ll give the chatbot more room to grow
#passign a list of two strings
#.train() injects entries into your database to build upon
#trainer.train([
    #"Hi",
    #"Welcome, buddy",
#])
#trainer.train([
    #"How's the weather today?",
    #"Cloudy with a chance of meatballs!"
#])

exit_conditions = (":q", "quit", "exit")
#while loop that’ll keep looping unless you enter one of the exit conditions
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f" {chatbot.get_response(query)}")
#.get_response() is the only interaction with your chatbot.