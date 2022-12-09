import streamlit as st

movie_genres = [None,
                '(no genres listed)',
                'Action',
                'Adventure',
                'Animation',
                'Children',
                'Comedy',
                'Crime',
                'Documentary',
                'Drama',
                'Fantasy',
                'Film-Noir',
                'Horror',
                'IMAX',
                'Musical',
                'Mystery',
                'Romance',
                'Sci-Fi',
                'Thriller',
                'War',
                'Western'
                ]


def run_streamlit():
    st.set_page_config(page_title="Movie Recommender", page_icon="🤖")
    with st.form("Recommend me!"):
        st.header("Enter below info")
        user_id = st.text_input("Enter User id: ", "", max_chars=4)
        genre = st.selectbox("Select movie genre", movie_genres)
        submit_btn = st.form_submit_button("Recommend me!")

        if submit_btn:
            with st.spinner('Wait for it...'):
                from get_movies import UIMovieRecommendation
                data_input = {
                    "user_id": user_id,
                    "genre": genre
                }

                try:
                    recommended_movies = UIMovieRecommendation(
                    data=data_input
                    ).get_recommended_movies()
                except Exception as e:
                    st.error(e)
                else:
                    st.table(recommended_movies)

    if st.button("New user?"):
        with st.form("Add information"):
            user_mail = st.text_input("email adress")
            favorite_movie = st.text_input("Your favorite movie is...")
            if st.form_submit_button("send"):
                with st.spinner('Welcome! Please make yourself comfortable till I...'):
                    ##some code to update our user database
                    ###some code to email user_id
                    st.text("Congrats! Check the mailbox for your user_id!")
                    import time
                    time.sleep(3)


if __name__ == "__main__":
    run_streamlit()
