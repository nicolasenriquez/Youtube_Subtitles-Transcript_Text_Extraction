import datetime
import pandas as pd
import numpy as np


# Read .txt file and return a DataFrame
def from_text_to_dataframe(file_name):
    """
    This function recives the path of the text file that stores the video transcrypt and returns a dataframe with a column
    that stores the time and the other that holds the subtitle text of that specific timestamp.
    """
    with open(file_name, 'r') as f:
        video_transcript_text = f.read()

    words = [text for text in video_transcript_text.splitlines()]
    text_with_time = [{'time': words[i], 'text': words[i+1]} for i in range(0, len(words)-1, 2)]
    transcript_df = pd.DataFrame(text_with_time)

    return transcript_df


# Clean the dataframe and remove the quotes
def clean_dataframe(df):
    """
    This function helps to clean the dataframe, it deals with the time in order to transform it into a time object, and drops the
    rows from the dataframe that holds "[ quotes ] using regex" 
    """
    # Add the Hour to the Time in order transform it from string to datetime
    df['time'] = df['time'].apply(lambda x: '00:' + x)
    df['time'] = df['time'].apply(lambda x: datetime.datetime.strptime(x, '%H:%M:%S'))
    # Remove rows from the dataframe the text [] quotes like: [Music]
    df = df[~df['text'].str.contains(pat='\[\w*\]')].reset_index(drop=True)

    return df


# Search for the previous possible timestamp in the text transcript dataframe
def find_previous_timestamp_in_df(df, guess_minutes, guess_seconds):
    """
    This function helps to retrieve the previos possible timestamp with its index position in
    the transcript, this is done by performing a search with a guessed timestamp using the a
    datetime.datetime object.
    """
    guess_date = datetime.datetime(1900, 1, 1, 00, minute=guess_minutes, second=guess_seconds)
    last_row = df[df['time'] <= guess_date].iloc[-1, :]
    
    return last_row['time']


# Return a specific text segment selected from between ranges of time from inside the transcript
def extract_text_section_from_transcript(df, start_mins, start_secs, end_mins, end_secs, question_number=None, question_title=None):
    """
    This function will return the complete text of a specific section of the transcript using as bounds the beginning and the
    ending time specified in the fuction, the times provided will be corrected with the function find_previous_timestamp_in_df().
    """
    begin_time = find_previous_timestamp_in_df(df, guess_minutes=start_mins, guess_seconds=start_secs)
    end_time = find_previous_timestamp_in_df(df, guess_minutes=end_mins, guess_seconds=end_secs)
    text_header = f"Question #{question_number} - {question_title}"
    text_body = str(" ".join(df[(df['time'] >= begin_time) & (df['time'] <= end_time)]['text'].values))
    full_text = text_header + '\n\n' + text_body + '\n\n'

    return full_text


# Creates the final report and optionally, can save it as a .txt file
def elaborate_report(report_title, questions_list, save_as_txt=False):
    """
    This function helps to compile all the questions into a one structured Data Report with the ability of saving it as a .txt file
    in the same folder that you are running the script and named using the report title and the current date.
    """
    report_text = f"Created at {datetime.datetime.now()}\n\n{report_title}\n\n\n"
    
    for question in questions_list:
        report_text += question

    if save_as_txt:
        with open(f"{report_title}_{datetime.date.today()}.txt", 'w') as f:
            f.write(report_text)
            print(F"File Saved Successfully!")

    return report_text    