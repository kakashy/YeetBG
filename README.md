# YeetBG

YeetBG is a web application that removes the background from images. It features:

- A SvelteKit frontend using TailwindCSS and Shadcn-Svelte.
- A FastAPI backend powered by Rembg for background removal.

## Project Structure:

- frontend/ : SvelteKit frontend
- backend/ : FastAPI backend
- docker-compose.yml
- README.md

## Prerequisites:

- Docker
- Docker Compose

## Getting Started:

### 1. Clone the repository

- Run `git clone https://github.com/kakashy/yeetbg.git`
- Navigate into the project directory with `cd yeetbg`

### 2. Build and Run the Project

#### With Docker Compose:

- To build and start both the frontend and backend services, run `docker-compose up --build`.
- If no changes were made to the Dockerfiles, you can omit the `--build` flag: `docker-compose up`.

#### Individual Services:

To build and run the backend:

- Navigate to the backend directory with `cd backend`.
- Build the Docker image with `docker build -t yeetbg-backend .`.
- Run the backend with `docker run -p 8000:8000 yeetbg-backend`.

To build and run the frontend:

- Navigate to the frontend directory with `cd frontend`.
- Build the Docker image with `docker build -t yeetbg-frontend .`.
- Run the frontend with `docker run -p 3000:3000 yeetbg-frontend`.

### 3. Access the Application

- Frontend: Open your browser and go to http://localhost:5173
- Backend: Open your browser and go to http://localhost:8000/docs to access FastAPI Swagger

### 4. Stopping Services

- To stop the services, run `docker-compose down`.

## Contributing:

Feel free to fork this repository, create a feature branch, and submit a pull request.

## License:

This project is licensed under the MIT License.
