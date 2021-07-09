import pickle
import streamlit as st
import numpy as np
import pandas as pd
import requests

st.header('Book Recommendation System')

def fetch_poster(isbn):
    url="http://covers.openlibrary.org/b/isbn/{}-M.jpg".format(isbn)
    st.text(url)
    return url

books=pd.read_pickle(open('books.pkl','rb'))
similarity=pickle.load(open('books_similarity.pkl','rb'))
#books.drop_duplicates(subset='title',keep='first',inplace=True)
books_list=np.sort(books['title'].unique())
#list=['Hi','Hello']
selected_book = st.selectbox('Search Book Name',books_list)

def recommend(book_name):
    index=books[books['title']==book_name].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    books_names=[]
    books_images=[]
    for i in distance[1:6]:
        books_isbn=books.iloc[i[0]].isbn13
        books_names.append(books.iloc[i[0]].title)
        books_images.append(fetch_poster(books_isbn))
    return books_names,books_images

if st.button('Show Recommendation'):
    books_names,books_images=recommend(selected_book)
    col1,col2,col3,col4,col5=st.beta_columns(5)
    with col1:
        st.text(books_names[0])
        st.image(books_images[0])
    with col2:
        st.text(books_names[1])
        st.image(books_images[1])
    with col3:
        st.text(books_names[2])
        st.image(books_images[2])
    with col4:
        st.text(books_names[3])
        st.image(books_images[3])
    with col5:
        st.text(books_names[4])
        st.image(books_images[4])
