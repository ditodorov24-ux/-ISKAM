import streamlit as st

st.title("Библиотека")

# Създаваме списък, ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# + Добавяне на книга
st.header("+ Добави книга")

title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

# Покажи всички книги
st.header("Всички книги")

if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("----")

# Търсене по заглавие
st.header("Търсене по заглавие")

search_title = st.text_input("Въведи заглавие за търсене")

if st.button("Търси по заглавие"):
    found = False
    for book in st.session_state.books:
        if book["title"].lower() == search_title.lower():
            st.write("Намерена книга:")
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерена такава книга.")

# Най-евтина книга
st.header("Най-евтина книга")

if st.button("Покажи най-евтината книга"):
    if len(st.session_state.books) == 0:
        st.write("Няма книги.")
    else:
        cheapest = min(st.session_state.books, key=lambda x: x["price"])
        st.write("Най-евтината книга е:")
        st.write(cheapest)


