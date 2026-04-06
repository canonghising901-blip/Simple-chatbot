def chatbot():
    print("Chatbot: Hello ! Type 'bye' to exit.")

    while True:
        user=input("You:").lower()

        if user=='hello' or user=="hi":
            print("Chatbot: Hi there!")
        elif user=='your name':
            print("Chatbot:I'm a simple python chatbot.created for timepass")
        elif user=='how are you':
            print("Chatbot:I'm just code, but I'm doing great anyway")
        elif user=='help':
            print("Chatbot:You can say hello,ask my name,or say bye")

        elif user=='bye':
            print("Chatbot:Goodbye")
            break
        else:
            print("Chatbot:Sorry,I can't understand that.\nYou can say hello,ask my name,or say bye") 

chatbot()