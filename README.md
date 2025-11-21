# Living With Mama
#### Video Demo:  <INSERT YOUTUBE LINK HERE LATER>
#### Description:

**Living With Mama** is a web-based platform designed to digitize the management of a peaceful home. It serves as a hybrid between a family utility tool and a niche marketplace, addressing the need for a centralized digital space where families can find inspiration, entertainment, and commerce focused on domestic comfort.

Unlike generic social networks or e-commerce sites, this application is specifically tailored for the "Home & Family" niche, combining utility (quizzes/tips) with commerce (family side-hustles).

### Key Features

1.  **The Family Market (CRUD Application):**
    A fully functional marketplace where users can list items for sale. This utilizes SQL Relational Databases to link users to their specific items. Users can:
    * List new items (Title, Price, Category, Description).
    * Search for items using a live, client-side JavaScript filter.
    * View contact details to arrange purchases.

2.  **The Homemaker Quiz (Game Logic):**
    An interactive trivia section that tests users on domestic knowledge (e.g., cleaning hacks, cooking safety).
    * It uses Python logic to calculate scores.
    * It saves results to the database to track history.

3.  **Inspiration Hub:**
    A curated section for recipes, gardening tips, and home decor ideas, served via Bootstrap cards for a clean, responsive UI.

4.  **User Authentication:**
    A secure system using `werkzeug.security` for password hashing, ensuring that user accounts are protected.

### Technical Implementation

The project is built using **Python (Flask)** for the backend and **SQLite** for database management.
* **Frontend:** HTML5, CSS3, and Bootstrap 5 for responsive design. Custom JavaScript is used for dynamic DOM manipulation (search filtering).
* **Backend:** Flask routes handle the logic for serving templates, processing forms, and managing sessions.
* **Database:** Three main tables (`users`, `market_items`, `quiz_scores`) linked via foreign keys to ensure data integrity.

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Initialize the database: `sqlite3 livingwithmama.db < schema.sql`
3. Run the application: `flask run`