# Movies Recommendation System

## Overview

The Movies Recommendation System is a data science project created by Akash Patil. It leverages content-based filtering and natural language processing (NLP) techniques to provide personalized movie recommendations.

## Live Demo

Explore the live demo of the Movies Recommendation System: [Demo Link](https://movies-recommendation-system-akash-patil.streamlit.app/)

## Dataset Source

The dataset used for this project contains metadata for more than 700,000 movies and is sourced from Kaggle's TMDB Dataset. You can access the dataset here: [Kaggle Dataset](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies/)

## Limited Resources

It's worth noting that this project was developed with limited resources. Despite the constraints, the project showcases the capabilities of content-based filtering and NLP techniques in providing valuable movie recommendations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

[... Rest of the README as previously provided ...]


## Installation

To run this project locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/akashpatil108/movies-recommendation-system.git
   ```

2. Change to the project directory:

   ```bash
   cd movies-recommendation-system
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Visit the live demo [here](https://movies-recommendation-system-akash-patil.streamlit.app/).

2. Select a movie title or enter a movie title in the input box.

3. Adjust the number of recommendations using the slider.

4. Click the "Recommend" button to get personalized movie recommendations based on your input.

5. If you want to apply a filter to the recommendations, follow these steps:
   - In the "Select the filter you want to apply" dropdown, choose from options like "genres," "original_language," "production_companies," or "release_year."
   - Select specific filter values in the dropdown that appears based on your choice.
   - The recommendations will be filtered according to your selection.

6. Explore the recommended movies and their details.


## Features

- Personalized movie recommendations based on user input.
- Interactive user interface built with Streamlit.
- Detailed movie information, including title, genres, language, overview, and more.

## Technologies Used

The Movies Recommendation System utilizes various technologies and libraries for data analysis, natural language processing, and user interface development, including:

- Streamlit: A Python library used to create interactive web applications.
- Python: The primary programming language for the project.
- Pandas: Used for data manipulation and analysis.
- Pillow: A library for working with images, used for displaying movie posters.
- Scikit-learn: Utilized for natural language processing and cosine similarity calculations.

For the model development and analysis in Jupyter Notebook, the following libraries were used:

- Numpy: A fundamental library for scientific computing with Python.
- Seaborn: A data visualization library based on Matplotlib, used for creating insightful visualizations.
- Matplotlib: A widely-used plotting library for creating static, animated, and interactive visualizations.
- Zipfile: Used for working with ZIP archives.
- OS: A library for interacting with the operating system.
- Regular Expressions (re): Employed for text preprocessing.
- NLTK: The Natural Language Toolkit for NLP tasks.
- Stopwords: NLTK's corpus of stop words for text cleaning.
- PorterStemmer: NLTK's stemming algorithm for text processing.
- CountVectorizer: Scikit-learn's tool for text feature extraction.
- Cosine Similarity: Scikit-learn's metric for calculating the similarity between movie descriptions.

These libraries and technologies collectively contribute to the functionality and features of the Movies Recommendation System, enabling personalized movie recommendations based on content analysis.



## Screenshots
![Screenshot 2](https://github.com/akashpatil108/movies-recommendation-system/blob/962f7d4bc6045620a6c33c214194362ebc7d73f0/Screenshot%20(22).png)

![Screenshot 1](https://github.com/akashpatil108/movies-recommendation-system/blob/962f7d4bc6045620a6c33c214194362ebc7d73f0/Screenshot%20(20).png)



## License

This project is licensed under the [Your License Name](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to Akash Patil:

- LinkedIn: [Akash Patil LinkedIn](https://www.linkedin.com/in/akash-patil-985a7a179/)
- GitHub: [Akash Patil GitHub](https://github.com/akashpatil108)


## Acknowledgments
## Acknowledgments

We would like to express our gratitude to the following individuals, organizations, and platforms for their invaluable contributions and support in the development of the Movies Recommendation System:

- **TMDB (The Movie Database)**: Our project utilizes data and images sourced from TMDB. TMDB provides a comprehensive database of movie information and images, which has been instrumental in enhancing the content and visual appeal of our recommendation system.

- **Kaggle**: We extend our thanks to Kaggle for hosting and making available the TMDB Dataset. Kaggle's platform has been a valuable resource for accessing and working with this dataset.

- **Open Source Community**: Our project builds upon the collective knowledge and efforts of the open-source community. We appreciate the countless open-source libraries, tools, and resources that have made this project possible.

- **GitHub**: We utilize GitHub as a collaborative platform for code hosting and version control. GitHub's features and ecosystem have facilitated the development and sharing of this project.

- **Streamlit Community**: We appreciate the Streamlit community for creating an accessible platform that enables us to build interactive web applications with ease.

- **Python and Data Science Community**: Our project leverages Python and various data science libraries. We are thankful for the Python and data science communities for their continuous support and advancements in the field.

Your support and contributions, along with the availability of TMDB data and images, have been essential in making this project a reality. We look forward to continued collaboration and improvement in the future.



