# Reviews in a .txt file with \n separator for each review

import math
import openai

openai.api_key = "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"
model_engine = "text-davinci-002"
filename = r"D:\MSAI\sem 2\SWM\project\reviews.txt"
pos = 0
neg = 0
c = 0
pos_sent = ''
neg_sent = ''
with open(filename, 'r') as file:
    # read the contents of the file and split it based on the newline character
    lines = file.read().split('\n')
    for line in lines:
        c += 1
        prompt = (
            f"Please analyze the following text and return the sentiment in positive or negative only:\n\n"
            f"{line}\n\n"
            f"Sentiment:"
        )
        # Call the OpenAI API and retrieve the sentiment analysis results
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
        )
        # Extract the sentiment from the API response
        sentiment = response.choices[0].text.strip()
        if sentiment == 'Positive' or sentiment == 'positive':
            pos += 1  # count positive reviews
            pos_sent = pos_sent + line  # join positive reviews
        elif sentiment == 'Negative' or sentiment == 'negative':
            neg += 1
            neg_sent = neg_sent + line
        print('review ', c, ' : ', sentiment)
print('positive reviews = ', pos)
print('negative reviews = ', neg)
# print('positive sentiments ', pos_sent)
# print('negative sentiments ', neg_sent)


def summarize_text(text):
    # instruct = "Please extract most meaningful few sentences, and make a summary of them in one paragraph,
    # " \ "describing as third person in a total of " + str(pos_sentences) + " sentences only , and dont iclude
    # numbering, " \ "just 1 paragraph :\n\n" \ "{}".format(text) Send a request to the OpenAI API to generate a
    # summary of the input text
    instruct = "Please analyze the following user reviews and return the summary : \n\n{}".format(text)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=instruct,
        temperature=0.8,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Extract the generated summary from the API response
    summary = response.choices[0].text.strip()
    # Return the summary
    return summary


all_reviews = pos_sent + neg_sent
all_summary = summarize_text(lines)
sentiment_summary = 'Dear user, there were total of ' + str(c) + ' reviews for this item, out of which ', pos, 'were positive and ', neg, ' were negative'
print(sentiment_summary)
print("{}".format(all_summary))
#
# if pos >= neg and pos != 0:
#     if pos < 3:
#         pos_sentences = 1
#     elif 2 < pos < 5:
#         pos_sentences = 4
#     elif 4 < pos < 10:
#         pos_sentences = 5
#     elif 9 < pos:
#         pos_sentences = 6
# # summary of positive reviews
# pos_summary = summarize_text(pos_sent)
# # print("Original text: {}".format(pos_sent))
# # print("Generated summary: {}".format(pos_summary))
#
# # # summary of negative reviews
# # if pos != 0 and neg != 0:
# #     if neg < 3:
# #         neg_sentences = 1
# #     elif 2 < neg < 5:
# #         neg_sentences = 4
# #     elif 4 < neg < 10:
# #         neg_sentences = 5
# #     elif 9 < pos:
# #         neg_sentences = 6
#     # summary of positive reviews
# if neg>0:
#     neg_summary = summarize_text(neg_sent)
#     print("Original text: {}".format(pos_sent))
#     print("Generated summary: {}".format(neg_summary))
# elif neg==0:
#     neg_summary = 'Not a single negative review found'
# sentiment_summary = 'Dear user, there were total of ' + str(
#     c) + ' reviews for this item, out of which ', pos, 'were positive and ', neg, ' were negative'
# reviews_summary = pos_summary + neg_summary if pos > neg else neg_summary + pos_summary
# import re
# pos_summary_filtered = re.split(r'\d', pos_summary, maxsplit=1)[0]
# neg_summary_filtered = re.split(r'\d', neg_summary, maxsplit=1)[0]
# print('\n\n*************AI generated summary is ***************** ')
# print(sentiment_summary)
# print(pos_summary_filtered)
# print(neg_summary_filtered)


#
# if pos != 0 and neg != 0:
#     if pos > neg:
#         ratio = pos / neg
#     elif neg > pos:
#         ratio = neg / pos
#     elif pos == neg:
#         ratio = 1
