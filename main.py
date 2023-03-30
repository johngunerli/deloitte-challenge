'''
TODO: 

-get class information from either a place like course-critique or sth, or gt-scheduler, you can a also use the gt class wiki, summarize them, and check if the users words align well with the class description

- get all the class requirements for a thread in cs and store them somewhere 

-make this in streamlit 

'''

# TODO: 
# first, we'd need to scrape data. for now, i'm simply going to be using data from the url mentioned in scrape.py 
# put these into a dictionary where the key is the thread name, and the value is the description 

thread_to_concept = {
    "Devices": "programming for embedded devices",
    "Information Internetworks": "representing and transmitting information",
    "Intelligence": "artificial intelligence, machine learning, computer vision",
    "Media": "information visualization, video game development, new media",
    "Modeling and Simulation": "high-performance computing, modeling complex systems and phenomena",
    "People": "user experience research, human-computer interaction, product design",
    "Systems and Architecture": "computer operating systems, compilers, languages",
    "Theory": "theoretical computer science"
}



user_input = input("What subject matter are you most interested in?")


# take the root of each value in the dictionary above, and compare it with the root of the user input, and return the key with the highest ratio between the two
all_threads = list(thread_to_concept.keys())
all_descriptions = list(thread_to_concept.values())

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

stemmed_descriptions = [stemmer.stem(description) for description in all_descriptions]

stemmed_user_input = stemmer.stem(user_input)

# compare the user input with each of the descriptions, and return the key with the highest ratio between the two

from difflib import SequenceMatcher

ratios = [SequenceMatcher(None, stemmed_user_input, stemmed_description).ratio() for stemmed_description in stemmed_descriptions]

# print ratios with the corresponding thread name

# put all these ratios into a dictionary where the key is the thread name, and the value is the ratio

thread_to_ratio = dict(zip(all_threads, ratios))

# print the thread with the highest ratio

print(max(thread_to_ratio, key=thread_to_ratio.get))
    


# ALTERNATIVE APPROACH: use AI from huggingface


# then we need to get this scraped data to be summarized using some sort of model @ huggingface 
# FIXME: for now use the one below, but we can change it later


from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

# result = question_answerer(question=user_input, context=context)
# print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

# we can then check if the users' input box aligns well with any of the possible class options we hold in our database (we might need to do some NLP stuff here)
# such as comparing the root words agains the user input's root words and check which one brings the most ratio between the two 





