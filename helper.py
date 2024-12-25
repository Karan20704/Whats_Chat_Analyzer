from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji


extractor = URLExtract()


def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    # number of messages
    num_messages = df.shape[0]

    # number word
    word = []
    for message in df['message']:
        word.extend(message.split())

    # number of media acces
    num_media = df[df['message']=='<Media omitted>'].shape[0]
    
    # number of link
    link = []
    for message in df['message']:
        link.extend(extractor.find_urls(message))
 
    return num_messages,len(word),num_media,len(link)

# most bussy
def most_bussy_user(df):
    x = df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'Name','count':'Precent'})

    return x,df

# wordcloud
def create_word_cloud(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user']==selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>']

    def remove_stopword(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    
    temp = temp['message'].apply(remove_stopword)
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(temp.str.cat(sep=" "))

    return df_wc

def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()
        
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
          if word not in stop_words:
             words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    most_common_df = most_common_df.rename(columns={0:'word',1:'count'})

    return most_common_df

def emoji_helper(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user']==selected_user]

    emojis = []
    for message in df['message'].dropna():
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    new_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return new_df

def timeline_helper(selected_user,df):
        
        if selected_user != 'Overall':
           df = df[df['user']==selected_user]
    
        timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()

        time = []
        for i in range(timeline.shape[0]):
           time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
        
        timeline['time'] = time

        return timeline

def daily_timeline_helper(selected_user,df):
            if selected_user != 'Overall':
                 df = df[df['user']==selected_user]

            daily_timeline = df.groupby('only_date').count()['message'].reset_index()

            return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
         df = df[df['user']==selected_user]

    return df['day_name'].value_counts()


def monthly_activity_map(selected_user,df):

    if selected_user != 'Overall':
         df = df[df['user']==selected_user]

    return df['month'].value_counts()

def heatmap_analysis(selected_user,df):

    if selected_user != 'Overall':
         df = df[df['user']==selected_user]  

    activity_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return activity_heatmap