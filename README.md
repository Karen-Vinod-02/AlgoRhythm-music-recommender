# AlgoRhythm

AlgoRhythm is a content-based music recommendation system that uses a rule-based filtering engine to suggest songs based on user input. Users can log in and enter keywords such as mood, genre, or artist into the search bar to receive recommendations from a preloaded CSV dataset.

The system uses hybrid rule-based content filtering system to provide recommendations. Built using Django, it offers a lightweight and extendable web interface for exploring songs by mood, tempo, and genre.

---

## Features

- User login and authentication system
- Search bar for artist/title/mood based queries
- Real-time filtering based on song metadata
- Rule-based filtering logic 
- CSV-backed dataset (no database required for content)
- Clean Django-based frontend 

---

## Tech Stack

- **Backend**: Python, Django  
- **Frontend**: HTML/CSS
- **Authentication**: Django auth system  
- **Dataset Format**: CSV

---

## Dataset

**Source**:  
[https://www.kaggle.com/datasets/jashanjeetsinghhh/songs-dataset](https://www.kaggle.com/datasets/jashanjeetsinghhh/songs-dataset)

**Structure**:  
The dataset contains columns such as:
- Track Name
- Artist
- Image
- Energy
- Danceability
- Speechiness

The CSV file is preloaded under the `musicrec_app/data/` directory.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Karen-Vinod-02/AlgoRhythm-music-recommender.git
cd AlgoRhythm
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```
### 3. Configure Environment Variables
This project uses a .env file to manage sensitive settings . You would need to create your own Django secret key.
- In the root directory of the project, create a file named `.env`.
- Add the following line to the file:
``` 
DJANGO_SECRET_KEY= #your-secure-secret-key
```

**Note**: If DJANGO_SECRET_KEY is not set in the environment, the app will raise an error when starting. This is handled in settings.py for security.

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Create a superuser(for access to admin panel)
```
python manage.py createsuperuser
```
Follow the prompts to set admin's username, email, and password.

## Running the Project
```
python manage.py runserver
```
Then open your browser and visit:
http://127.0.0.1:8000/

## Acknowledgements
- Music.csv Dataset – [Kaggle](https://www.kaggle.com/datasets/jashanjeetsinghhh/songs-dataset)
