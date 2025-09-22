import textwrap

story ='''Welcome to Private jet! A game whare you can win money by answering aviation related questions! Are you true plane enthusiast?
Can you name every airport by drop of a hat? This is a game for you!
On each round you will be asked one question and you have to choose an answer from four options. There will be x rounds.
If you can not answer the question you may use 50/50, Ask the audience or Call a friend.
50/50 will eliminate half of your options. Ask the audience will give percentage of people that think that the option is correct. Call a Friend will suggest one answer. 
 x times you will be given a chance to give up, take the money and run. But if you persist till the end the grand price of 1 000 000€ awaits you!
Ready to play? Good luck! '''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list