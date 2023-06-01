#  Develop an elementary chatbot for any suitable customer interaction application

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('MyChatBot')
trainer = ListTrainer(chatbot)
training_data = [
    ["Hi there!", "Hello! How can I assist you today?"],
    ["What services do you offer?", "We offer a wide range of services to cater to different needs."],
    ["How can I contact customer support?", "You can reach our customer support team at support@example.com."],
    # Add more conversation pairs here
]
trainer.train(training_data)
response = chatbot.get_response('Hello')
print(response)



