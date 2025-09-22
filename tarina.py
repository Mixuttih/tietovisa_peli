import textwrap

story ='''Welcome to Private jet! A game whare you can win money by answering aviation related questions! Are you true plane enthusiast?
Can you name every airport by drop of a hat? This is a game for you!

'''

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=story)


def getStory():
    return word_list