import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
st.title (" SENTIMENT ANALYSS SYSTEM ")
choice=st.sidebar.selectbox("My Menu",("HOME","ANALYSYS","VISUALIZATIONS"))
if(choice== "HOME"):
    st.image("https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/202/619/datas/original.gif")
    st.write("This project is developed by P.Rahul_Shyamkumar as part of project-3")
elif(choice==" ANALYSIS"):
    url=st.text_input("Enter google sheet URL")
    c=st.text_input("Enter Column to be analyzed")
    btn=s.button("Analyze")
    if btn:
        mymodel=SentimentIntensityAnalyzer()
        df=pd.read_csv(url)
        X=df[c]
        l=[]
        for k in X:
          pred=mymodel.polarity_scores(k)
          if(pred['compound']>0.05):
            l.append("Positive")
          elif(pred['compound']<-0.05):
	    l.append ("Negative")
	  else:
            l.append("Neural")
        df['Sentiment']=1
        df.to_csv("results.csv",index=False)
        st.subheader("Analysis Sucessfull and results are saved as results.csv")
        
 '''   if(choice=="VISUALIZATIONS"): df=pd.read_csv("results.csv")
        st.dataframe("https://docs.google.com/forms/d/e/1FAIpQLSejAzqdBeRdQZ3bhOTQE2SXjWhuhEsrWlLEBvaUFOUUMUgjCA/viewform?usp=header")
choi  ce2=st.selectbox("Choose Visualization",("NONE", "PIE", "HISTOGRAM")) if(choice2=="PIE"):
        posper=(len(df[df['Sentiment']=="Positive"])/len(df))*100 negper=(len(df[df['Sentiment']=="Negative"])/len(df))*100 neuper=(len(df[df['Sentiment']=="Neutral"])/len(df))*100
        fig=px.pie(values=[posper,negper,neuper],names= ['Positive', 'Negative', 'Neutral']) st.plotly_chart(fig) elif(choice2=="HISTOGRAM"):
        C=st.selectbox("Choose Columns",df.columns)
        if c:
            fig=px.histogram(x=df[c].color=df['Sentiment'])
            st.plotly_chart(fig)

'''
