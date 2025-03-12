# Festivo - Music Festival Artist Recommender

## About
Festivo is a web application that helps festival-goers discover new artists based on their Spotify listening history.

## Tech Stack  

### Frontend  
- **React** – UI framework  
- **TypeScript** – Type-safe development  
- **React Query** – Efficient data fetching & caching  
- **Zustand / Redux Toolkit** – State management (TBD)  
- **Vite** – Fast build tool  
- **Tailwind CSS** – Utility-first styling  

### Backend  
- **FastAPI** – High-performance Python API framework  
- **SQLAlchemy** – ORM for database management  
- **OAuth (Spotify)** – User authentication & authorization  
- **Redis** – Caching layer for performance optimization  
- **Alembic** – Database migrations  

### Database  
- **PostgreSQL** – Relational database for storing user, artist, and track data  

### Deployment  
- **Docker Compose** – Local development setup  
- **AWS ECS** (Planned) – Production deployment   

## Setup  
1. Clone the repo  
2. Install dependencies (`pip install -r requirements.txt`)  
3. Set up `.env` with Spotify API keys  
4. Run with Docker Compose (`docker-compose up --build`)  

_For detailed progress updates, check out [`DEVLOG.md`](DEVLOG.md)._  
