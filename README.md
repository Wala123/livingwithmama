# Living With Mama

#### Video Demo: [Paste your YouTube URL here]

#### Description:
Living With Mama is a web-based platform designed to digitize the management of a peaceful home. It serves as a hybrid between a family utility tool and a niche marketplace, providing a centralized digital space where families can find inspiration, entertainment, and commerce focused on domestic comfort.

Unlike generic social networks or e-commerce sites, this application is tailored specifically for the Home & Family niche—combining utility (quizzes/tips) with commerce (family side-hustles).

### Key Features

1. **The Family Market (CRUD Application):**  
   A functional marketplace where users can list items for sale. This uses SQL relational databases to link users to their specific items. Users can:  
   - Add new items (Title, Price, Category, Description)  
   - Search for items via a live JavaScript filter  
   - View contact details to arrange purchases  

2. **The Homemaker Quiz (Game Logic):**  
   An interactive trivia section that tests users on domestic knowledge (cleaning hacks, cooking safety, etc.).  
   - Python logic calculates scores  
   - Results are saved to the database to track history  

3. **Inspiration Hub:**  
   A curated space for recipes, gardening tips, and home-decor ideas, built using Bootstrap cards for a clean, responsive layout.  

4. **User Authentication:**  
   A secure login system using Werkzeug.security for password hashing to ensure account protection.  

### Technical Implementation
The project is built using Python (Flask) for the backend and SQLite for database management.  

**Frontend:**  
HTML5, CSS3, Bootstrap 5 for responsiveness, and custom JavaScript (DOM manipulation, live search filtering).  

**Backend:**  
Flask routes handle template rendering, form processing, and session management.  

**Database:**  
Three main tables — users, market_items, quiz_scores — linked via foreign keys for data integrity.  

### How to Run

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Initialize the database:  
   ```bash
   sqlite3 livingwithmama.db < schema.sql
   ```

3. Run the application:  
   ```bash
   flask run
   ```

### Credits
**Research & Inspiration:**  
YouTube tutorials, documentation, blogs, community forums  

**AI Assistance:**  
ChatGPT, Gemini, Grok, Qwen  

**Design & Branding:**  
Created personally — logo, colors, typography, and full visual identity  

**Images:**  
Unsplash and Nano Banana illustrations  

**Code & Learning Support:**  
CS50x 2025 materials, edX, Khan Academy, CSGuide New Zealand, and other online communities  

**NB:**  
I may have lost track of every specific source I used. What I do know is that I learned from many places—online and offline—to fix errors, solve bugs, improve styling, and understand new concepts, terms, commands, and functions. In summary, I can't list every piece of help I received, but I am grateful for the journey and the final result. It led to the exact execution of what I envisioned.