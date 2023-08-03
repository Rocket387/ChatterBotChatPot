import re
#imports regex

def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+, \s\d+:\d+)" # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s" # " - "
    username = r"([\w\s]+)" # e.g. "Martin"
    metadata_end = r":\s" # ": "
    pattern = date_time + dash_whitespace + username + metadata_end
    #concatenates the regex patterns defined above as in the .txt file

    with open(chat_export_file, "r") as corpus_file:  #Corpus data is user contributed hence corpus_file
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content) # searches for all the instances of pattern
    # and replaces then with an empty string (deletes the patterns)
    return tuple(cleaned_corpus.split("\n"))
#splits the file content string into list items using .split("\n").

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]
#removes the first introduction line
    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus