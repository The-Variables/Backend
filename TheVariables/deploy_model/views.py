from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import spacy
import PyPDF2
import en_core_web_sm
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def extract_skills(resume_text):
    # nlp = en_core_web_sm.load()
    nlp = spacy.load('en_core_web_sm')
    nlp_text = nlp(resume_text)
    noun_chunks = nlp(resume_text).noun_chunks
    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]

class SkillExtractor(APIView):
    def post(self, request):
        fFileObj = open('Resume.pdf', 'rb')
        pdfReader = PyPDF2.PdfReader(fFileObj)
        pageObj = pdfReader.pages[0]
        resume = pageObj.extract_text()
        skills = extract_skills(resume)
        # print(skills)
        return Response({'data': skills})


class SentimentalModelAPI(APIView):
    def post(self, request):
        sid = SentimentIntensityAnalyzer()
        scores_negative = []
        scores_positive = []
        scores_neutral = []
        scores_compound = []
        sentence_sentiment_score = sid.polarity_scores(request.data.get('sentence','no'))    
        scores_negative.append(sentence_sentiment_score['neg']*100)
        scores_positive.append(sentence_sentiment_score['neu']*100)
        scores_neutral.append(sentence_sentiment_score['pos']*100)
        scores_compound.append(sentence_sentiment_score['compound']*100)
        return Response({'-ve':scores_negative,'+ve':scores_positive,'meh':scores_neutral,'avg':scores_compound})        
