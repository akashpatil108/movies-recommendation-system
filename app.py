import streamlit as st
import pandas as pd
import pickle
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

# Load the cleaned dataset
df = pd.read_csv("J:\\data science\\VS code\\movies recommendation system\\Movies_cleaned.csv")

# Create a copy of the original DataFrame
new_df = df.copy()

# Load the similarity matrix
similarity_matrix = "J:\\data science\\VS code\\movies recommendation system\\similarity_matrix.pkl"

with open(similarity_matrix, "rb") as f:
    similarity_matrix = pickle.load(f)

# Define a placeholder variable for recommended movies
recommended_movies = None

# Define a placeholder function for movie recommendations
def recommend_similar_movies(movie_title, df, similarity_matrix, num_recommendations=5):
    try:
        movie_index = df[df['title'] == movie_title].index[0]
    except IndexError:
        return None  # Return None if the movie title is not found in the dataset

    distances = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num_recommendations + 1]
    recommended_movies_df = df.iloc[[i[0] for i in movies_list]]
    return recommended_movies_df

# Streamlit UI components
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Add the CSS code to the Streamlit app
st.markdown('''
<style>
.top-corner-text {
  position: fixed;
  top: 0;
  left: 0;
  padding: 10px;
  background-color: #ffffff;
}
</style>
''', unsafe_allow_html=True)

# Add the text to the top corner of the web page
st.markdown('<div class="top-corner-text">to follow more updates [LinkedIn](https://www.linkedin.com/in/akash-patil-985a7a179/) [GitHub](https://github.com/akashpatil108) Akash Patil</div>', unsafe_allow_html=True)

st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
}
.header {
    padding: 20px;
    background-color: #70cdff;
    color: white;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
}
.sub-header{
    text-align: center;
}
.recommend-button-container {
    display: flex;
    justify-content: center;
}
.recommend-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    margin: 10px 0;
    cursor: pointer;
    transition-duration: 0.4s;
}
.recommend-button:hover {
    background-color: #45a049;
}
.movie-card {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    margin-top: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}
.expander-background {
    background-color: #YOUR_BACKGROUND_COLOR;
}
</style>
""", unsafe_allow_html=True)

# Stylish header
st.markdown('<div class="header">Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header"> A Data Science Project by Akash Patil</div>', unsafe_allow_html=True)
st.markdown('''[LinkedIn](https://www.linkedin.com/in/akash-patil-985a7a179/)
[GitHub](https://github.com/akashpatil108)
''')
st.markdown("---")

column = st.selectbox("Select the filter you want to apply", ["None", "genres", "original_language", "production_companies", "release_year"], key="a")

if column == "None":
    # Reset the filter, show all data
    new_df = new_df
else:
    unique_values = st.selectbox(f"Apply the filter to {column}", new_df[column].unique(), index=None, placeholder="Select the values", key="b")
    if unique_values:
        new_df = new_df[new_df[column] == unique_values]

# User input for movie title
user_input = st.selectbox("Enter a movie title:", new_df['title'].values, index=None, placeholder="Type or Select the movie...",)
st.write('You selected the movie:', user_input)

# Number of recommendations slider
num_recommendations = st.slider("Number of Recommendations", 1, 10, 5)

# Recommendation button with a stylish icon
if st.button("Recommend", key="recommend_button", help="Click to get movie recommendations"):
    # Logic for making recommendations based on user input
    recommended_movies = recommend_similar_movies(user_input, df, similarity_matrix, num_recommendations)

if user_input:
    selected_movie = df[df['title'] == user_input]
    SM_poster_path = selected_movie['poster_path'].values[0]
    st.subheader(f"Information about Selected Movie: **{user_input}**")
    st.image(f"https://image.tmdb.org/t/p/original/{SM_poster_path}", width=300)
    with st.expander(f"{selected_movie['title'].values[0]}"):
        st.write(f"**Title:** {selected_movie['title'].values[0]}")
        st.write(f"**Genres:** {selected_movie['genres'].values[0]}")
        st.write(f"**Language:** {selected_movie['original_language'].values[0]}")
        st.write(f"**Overview:** {selected_movie['overview'].values[0]}")
        st.write(f"**credits:** {selected_movie['credits'].values[0]}")
        st.write(f"**Production Companies:** {selected_movie['production_companies'].values[0]}")
        st.write(f"**Budget:** {selected_movie['budget'].values[0]}")
        st.write(f"**Revenue:** {selected_movie['revenue'].values[0]}")
        st.write(f"**Runtime:** {selected_movie['runtime'].values[0]} minutes")

# Display recommended movies with stylish card layout
if recommended_movies is not None:
    st.markdown(f"## Top {num_recommendations} Recommended Movies")
    st.markdown("---")
    for i, (_, row) in enumerate(recommended_movies.iterrows(), start=1):
        movie_title = row['title']
        poster_path = row['poster_path']
        # Use an expander for each movie title with custom HTML style
        with st.expander(f"#### {i}. **{movie_title}**", expanded=False):
            st.image(f"https://image.tmdb.org/t/p/original/{poster_path}", width=300)
            st.write(f"**Title:** {row['title']}")
            st.write(f"**Genres:** {row['genres']}")
            st.write(f"**Language:** {row['original_language']}")
            st.write(f"**Overview:** {row['overview']}")
            st.write(f"**credits** {row['credits']}")
            st.write(f"**Production Companies:** {row['production_companies']}")
            # Check if budget is 0 and display 'NA' if true
            budget = row['budget']
            if budget == 0:
                budget = 'NA'
            st.write(f"**Budget:** {budget}")
            # Check if revenue is 0 and display 'NA' if true
            revenue = row['revenue']
            if revenue == 0:
                revenue = 'NA'
            st.write(f"**Revenue:** {revenue}")
            st.write(f"**Runtime:** {row['runtime']} minutes")

# Stylish footer
st.markdown("---")
st.write(f"Number of Movies in dataset: {df['title'].count()}")
st.markdown("---")
st.markdown("## About This Project")
st.markdown("""
Welcome to the Movie Recommendation System!
This project leverages content-based filtering and natural language processing (NLP) techniques to provide you with personalized movie recommendations. Here's how it works:
1. **Input Your Movie:** Enter the title of a movie you love in the provided input box.
2. **Get Tailored Recommendations:** Click the "Recommend" button, and our system will analyze the content and characteristics of your selected movie.
3. **Discover Similar Movies:** We'll then present you with a list of movies that share similarities with your chosen film. You can explore their titles, genres, language, overviews, popularity, production companies, budgets, revenues, and runtimes.
4. **Project Credit:** This data science project is proudly created by Akash Patil, and we're excited to bring it to you.
## Project Disclaimer
**Note**: While we strive to provide accurate and tailored movie recommendations, it's important to acknowledge the limitations of our recommendation system:
1. **Limited Dataset**: Our recommendation system relies on the available dataset, which may not include all movies, especially those with limited data or niche genres. As a result, there might be cases where we cannot recommend similar movies due to the absence of sufficient data.
2. **Data Availability**: Our recommendations are based on existing movie features such as genres, language, and production companies. If a selected movie has unique characteristics that do not match closely with other movies in the dataset, the system may struggle to find close matches.
3. **Continuous Improvement**: We are continuously working to enhance our recommendation algorithms and expand our dataset. As we collect more data and improve our models, we aim to provide better recommendations in the future.
4. **Explore and Enjoy**: If you do not receive recommendations for your selected movie, we encourage you to explore and enjoy the movie based on your own preferences. Your unique taste may lead you to hidden gems that our system hasn't discovered yet.
We appreciate your understanding and hope you find our Movie Recommendation System useful for discovering new movies that match your interests.
""")
