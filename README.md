# Movie Recommender System

This project is a Movie Recommender System built using Python and Streamlit. It allows users to select a movie from a list and get recommendations for similar movies, along with their posters fetched from the OMDb API.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Movie Recommendations**: Get a list of movies similar to the one selected.
- **Poster Display**: View movie posters alongside recommendations.
- **Simple Interface**: User-friendly interface built with Streamlit.

## Demo

You can try out the app 
https://movie-recommender-jpwlqsimhcwbgtdifyrbtp.streamlit.app/

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DungeonMaster96/Movie-Recommender.git
    cd Movie-Recommender
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Get your OMDb API key**:
    - Sign up at [OMDb API](http://www.omdbapi.com/apikey.aspx) to get an API key.
    - Replace the placeholder API key in the `app.py` file with your own.

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Select a movie** from the dropdown menu and click on "Recommend" to get similar movie suggestions along with their posters.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Used for building the web interface.
- **Pandas**: Data manipulation and analysis.
- **OMDb API**: Fetching movie posters.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request if you'd like to contribute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


# APP LINK
https://movie-recommender-jpwlqsimhcwbgtdifyrbtp.streamlit.app/
