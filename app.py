import streamlit  as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

upload_file = st.sidebar.file_uploader("Choose a file")
if upload_file is not None:
    bytes_data = upload_file.getvalue()
    # data in byte but want in string format
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df = preprocessor.preprocess(data)

    # st.dataframe(df)
    st.title('Top Stats')
    # fetch unique list
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("show analysis wrt",user_list)

    if st.sidebar.button("show analysis"):
        # stats 
        num_messages = helper.fetch_stats(selected_user,df)

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages[0])
        
        with col2:
            st.header("Total Word")
            st.title(num_messages[1])

        with col3:
            st.header("Media Share")
            st.title(num_messages[2])

        with col4:
            st.header("Link Shared")
            st.title(num_messages[3])

    # Monthly time line
        st.title("Monthly Time-Line")
        timeline = helper.timeline_helper(selected_user,df)

        fig,ax=plt.subplots()

        ax.plot(
             timeline['time'], timeline['message'], 
             marker='o', linestyle='-', color='b', label='Messages'
            )

        ax.set_title('Messages Over Time', fontsize=16)
        ax.set_xlabel('Time', fontsize=14)
        ax.set_ylabel('Number of Messages', fontsize=14)

        ax.set_xticks(range(len(timeline['time'])))  # Set x-ticks based on index
        ax.set_xticklabels(timeline['time'], rotation=45, fontsize=10)

        ax.grid(alpha=0.3)

        ax.legend(fontsize=12)

        st.pyplot(fig)


    #    daily time line
        st.title("Daily time line")
    
        daily_timeline = helper.daily_timeline_helper(selected_user,df)

        fig, ax = plt.subplots(figsize=(18, 10))
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], marker='o', linestyle='-', color='b')

        ax.set_title('Daily Messages Over Time', fontsize=16)
        ax.set_xlabel('Date', fontsize=14)
        ax.set_ylabel('Number of Messages', fontsize=14)
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        st.pyplot(fig)

    #   weekly analysis
        st.title("Activity Map")
        col1,col2 = st.columns(2)

        with col1:
            st.header("MOST BUSY DAY")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)

        with col2:
            st.header("MOST BUSY MONTH")
            busy_month = helper.monthly_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='orange')
            st.pyplot(fig)
        
        st.title("Weekly Activity Map")
        user_heatmap = helper.heatmap_analysis(selected_user,df)
        fig,ax=plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)


    # finding busy memeber in group
        if(selected_user == "Overall"):
            st.title("Most Busy user")
            x,new_df= helper.most_bussy_user(df)
            fig,ax=plt.subplots()

            col1,col2 = st.columns(2)
            
            with col1:
                ax.bar(x.index, x.values, 
                       color=['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9'], 
                       edgecolor='black', linewidth=1.5)
                ax.set_title('Most Busy Users', fontsize=18, fontweight='bold', color='#333333')
                ax.set_xlabel('User Names', fontsize=14, labelpad=10)
                ax.set_ylabel('Activity Count', fontsize=14, labelpad=10)
                ax.tick_params(axis='x', labelsize=8)
                ax.tick_params(axis='y', labelsize=12)
                ax.grid(axis='y', linestyle='--', alpha=0.6, color='gray')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df, width=700, height=400)

    # word cloud
    st.title("WordCloud")
    df_wc = helper.create_word_cloud(selected_user,df)
    fig,ax = plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)

    # most common word
    st.title("common words")
    most_common_df = helper.most_common_words(selected_user,df)

    col1,col2 = st.columns(2)
    fig,ax=plt.subplots()

    with col1:
         st.dataframe(most_common_df, width=700, height=600)
    with col2:
        x = most_common_df['word']
        y = most_common_df['count']
        ax.bar(x, y, color=['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9'] * (len(x) // 4 + 1),
        edgecolor='black', linewidth=1.5)
        ax.set_title('Most Common Words', fontsize=18, fontweight='bold', color='#333333')
        ax.set_xlabel('Words', fontsize=14, labelpad=10)
        ax.set_ylabel('Frequency', fontsize=14, labelpad=10)
        ax.tick_params(axis='x', labelsize=8, rotation=45)
        ax.tick_params(axis='y', labelsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.6, color='gray')
        st.pyplot(fig)

# emojis
    st.title("Emojis")
    emoji_df = helper.emoji_helper(selected_user,df)

    col1,col2 = st.columns(2)

    with col1:
        st.dataframe(emoji_df, width=700, height=400)

    with col2:
        fig,ax = plt.subplots()
        ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
        st.pyplot(fig)

