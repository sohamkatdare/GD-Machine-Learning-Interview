import pandas as pd
from collections import Counter

# load the dataset
emails = pd.read_csv('data/emails.csv')

# TODO: Preprocess the email data
# - Combine the 'subject' and 'body' columns into a single text field
# - Convert text to lowercase
# - Remove special characters and extra spaces

#stopwords to ignore 
STOPWORDS = set(["the", "is", "and", "to", "in", "for", "of", "on", "a", "an", 
                 "with", "at", "by", "this", "that", "from", "it", "as", "or"])

# TODO: Implement a function to find the most common words in emails
def get_most_common_words(n: int) -> dict:
    """
    Find the most frequently used words in the email dataset.

    Steps to implement:
    1. Combine all email text into one large string (use the preprocessed 'combined' column).
    2. Tokenize the text by splitting on spaces.
    3. Remove stopwords in the emails using the provided STOPWORDS set.
    4. Count the occurrences of each word.
    5. Return the top 'n' most frequent words as a dictionary {word: count}.

    Args:
        n (int): The number of top words to return.

    Returns:
        dict: A dictionary containing the top 'n' words and their counts.
    """
    pass  
    
    #Implement logic starting here

#testing
if __name__ == "__main__":
    print(get_most_common_words(5))  #top 5 most frequent words testing
