# 🎬 Movie Similarity Explorer - Neurodiversity-Friendly 
### CS 7250 · Final Visualization Project  
*interactive system for exploring movie similarity through feature-based and emotional models.*

---

## 🔗 Live Demo (Landing Page)
This is the **single URL** for the entire project:

👉 **https://movie-similarity-project-landing.onrender.com**

# 🌟 Project Overview

Movies are complex cultural artifacts that can be compared in many ways — by genre, content, emotion, and viewer perception. So we built the neurodiversity-friendly version to help explore the movies based on our users needs, offering a multi-layered understanding of film similarity from both **structural** and **affective** perspectives. Main features:

### 1. Feature-based 
### 2. Emotion-based 

---
# 1. Feature-based 
## Key Features
- **Simple Mode (Calm View)**  
  Minimalized visual noise with muted colors and limited node density.

- **Rich Mode (Deep Dive)**  
  Full network with detailed tag and genre encodings.

- **Interactive Components**
  - Hover for details-on-demand  
  - Click to recenter the network ("focus lock")  
  - Search with visual emphasis (orange halo)  
  - Smooth transitions to prevent disorientation  
  - Linked histogram for rating distributions  

### Design Principles
- Reduced visual clutter  
- Clear visual hierarchy  
- Consistent color coding  
- ADHD-friendly interaction logic  
- High-readability legends  
- Stable background context (prevents “getting lost”)  
---

# 2. Emotion-based  

## Key Features
- **Radial Layout** grouping movies by emotional similarity  
- **Node Color = Valence** (positive ↔ negative mood)  
- **Node Size = Audience Engagement** (mean rating or rating count)  
- **Click to Recenter** the network on any film  
- **Hover Tooltips** with metadata (genres, emotional profile)  
- **Two Modes**
  - Simplified (ADHD/autism-friendly)  
  - Intense (high-density emotional relationships)
- **Scatter View""
- **Comparing Movies**

# Deploy
Both explorers are Dash applications deployable locally and on Render.

## Running Locally
- Install requirements
- >> pip install -r requirements.txt
- Run the Dash app

## Deploying on Render (Web-Based)
- Push this project to GitHub
- On Render → New Web Service → select your repo
- Use these settings:
- >> Build Command
- >> pip install -r requirements.txt
- >> Start Command
- >> gunicorn app:server
- Render will auto-deploy your Dash web app and provide a sharable URL.

## Dataset License & Required Citation
This project uses the MovieLens 25M Dataset by GroupLens Research at the University of Minnesota.
Although the data is processed and transformed for visualization purposes, the original dataset is copyrighted and must be cited according to its license.

### Usage License Summary (from MovieLens)
The MovieLens dataset may be used for research purposes under conditions including:
You must not imply endorsement from the University of Minnesota or the GroupLens Research Group.
You must acknowledge and cite MovieLens in any publications or projects using the data.
Data (including transformed versions) may be redistributed only under the same license terms.
The dataset may not be used commercially without permission from GroupLens.
All dataset files are provided “as is” with no warranty.
GroupLens and the University of Minnesota are not liable for damages resulting from use of the dataset.

#### Required Citation
If you use this project or dataset in an academic setting, cite the official MovieLens dataset publication:

_F. Maxwell Harper and Joseph A. Konstan. 2015.
The MovieLens Datasets: History and Context.
ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4 (2015), 19:1–19:19.
DOI: https://doi.org/10.1145/2827872_

#### About MovieLens / GroupLens
GroupLens is a research group at the University of Minnesota focusing on:
recommender systems
online community behavior
social computing
digital libraries
ubiquitous computing
MovieLens provides the movie recommendation platform from which this dataset originates. Visit: https://movielens.org

## Acknowledgment
This visualization project does not claim ownership of the MovieLens dataset.
All data originates from MovieLens and is used respectfully in accordance with its research license.
Only cleaned, aggregated, and transformed versions of the data appear in the app.
