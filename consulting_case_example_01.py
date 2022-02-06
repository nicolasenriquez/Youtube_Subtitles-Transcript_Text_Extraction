import datetime
import pandas as pd
import numpy as np
import youtube_transcrypt_reporting as ytr


########################################################################################################################
#                                                           CASE #1
########################################################################################################################

########################################################################################################################
#               Build the DataFrame and Clean it to Store the Timestamp and the Text from The TouTube Transcript
########################################################################################################################

# Path for the .txt file
case_1_transcrypt_txt = "Data/00-case01_youtube_transcript_2022-02-04.txt"
# Store the text in a dataframe
transcript_df = ytr.from_text_to_dataframe(case_1_transcrypt_txt)
# Clean the dataframe
transcript_df = ytr.clean_dataframe(transcript_df)

########################################################################################################################
#         Begin Builind The Text Report going Side-By-Side with The Youtube Video and Save it as .txt File
########################################################################################################################

# Introduction
title_intro = "Intro"
introduction = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=00,
                                                start_secs=00,
                                                end_mins=00,
                                                end_secs=35,
                                                question_number=0,
                                                question_title=title_intro)
#print(report_text + introduction)

# Question 1
title_1 = "Is the Market Attractive for the Customer?"
question_1 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=00,
                                                start_secs=35,
                                                end_mins=10,
                                                end_secs=27,
                                                question_number=1,
                                                question_title=title_1)
#print(report_text + question_1)

# Question 2
title_2 = "Propose Ideas of How to Increase Sales"
question_2 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=10,
                                                start_secs=27,
                                                end_mins=16,
                                                end_secs=21,
                                                question_number=2,
                                                question_title=title_2)
#print(report_text + question_2)

# Question 3
title_3 = "Expanding on the last Question, Can you Think of more Bulletpoints Ideas?"
question_3 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=16,
                                                start_secs=21,
                                                end_mins=19,
                                                end_secs=29,
                                                question_number=3,
                                                question_title=title_3)
#print(report_text + question_3)

# Question 4
title_4 = "Based on the Following Market Scenario, Estimate the % Market Share of the Following 2 Years"
question_4 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=19,
                                                start_secs=29,
                                                end_mins=24,
                                                end_secs=46,
                                                question_number=4,
                                                question_title=title_4)
#print(report_text + question_4)

# Question 5
title_5 = "Based on the Following Market Scenario, Estimate the % Market Share of the Following 2 Years"
question_5 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=24,
                                                start_secs=46,
                                                end_mins=26,
                                                end_secs=33,
                                                question_number=5,
                                                question_title=title_5)
#print(report_text + question_5)

# Question 6
title_6 = "Your partial opinion just based on what you have what you know, should he acquire this business or not?"
question_6 = ytr.extract_text_section_from_transcript(transcript_df,
                                                start_mins=26,
                                                start_secs=34,
                                                end_mins=28,
                                                end_secs=4,
                                                question_number=6,
                                                question_title=title_6)
#print(report_text + question_6)

# Print and Save as .txt file the video report
questions = [introduction, question_1, question_2, question_3, question_4, question_5, question_6]

# Elaborate final report and save it as .txt file
#print(ytr.elaborate_report("CONSULTING CASE REPORT #1", questions, save_as_txt=False))
report_text = ytr.elaborate_report("CONSULTING CASE REPORT #1", questions, save_as_txt=False)


########################################################################################################################
#                                                           CASE #2
########################################################################################################################

########################################################################################################################
#               Build the DataFrame and Clean it to Store the Timestamp and the Text from The TouTube Transcript
########################################################################################################################

# Path for the .txt file
case_2_transcrypt_txt = "Data/01-case02_youtube_transcript_2022-02-04.txt"
# Store the text in a dataframe
transcript_2_df = ytr.from_text_to_dataframe(case_2_transcrypt_txt)
# Clean the dataframe
transcript_2_df = ytr.clean_dataframe(transcript_2_df)

########################################################################################################################
#         Begin Builind The Text Report going Side-By-Side with The Youtube Video and Save it as .txt File
########################################################################################################################
