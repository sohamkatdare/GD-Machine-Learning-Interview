# Machine Learning Engineer Task

You are tasked with building a Python script that processes a dataset of emails and analyzes word frequency to find the most commonly used words.

## Setup Instructions:
- Clone this repository onto your local machine and navigate to the project directory:
- Create a virtual environment & install dependencies from requirements.txt (pip3 install -r requirements.txt)

## Requirements:
- Preprocess the email data:
    - Remove special characters, extra spaces, and convert all text to lowercase.
    - Combine the subject and body columns into a single text field for each email.

- Analyze Word Frequency:
    - Implement a function get_most_common_words(n: int) -> dict
        - This function should:
            - Take an integer n as input (e.g., 5 for the top 5 most frequent words).
            - Tokenize the text by splitting on spaces.
            - Remove stopwords from the provided STOPWORDS set.
            - Count word occurrences across all emails.
            - Return a dictionary {word: count} for the top n most frequent words.
