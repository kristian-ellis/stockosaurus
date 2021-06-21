# stockosaurus
> web application designed to display stocks, cryptocurrencies and relevant news articles                                                                            
> developed using React for an interactive user experience

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Project Status](#project-status)
* [Contact](#contact)


## General Information
- stockosaurus is a project that utilises a React frontend with a Django backend to allow for rapid development of interactive web applications

- intended to display useful stock and crypto related information in an appealing, interactive and user friendly way

- more information can be found below, as well as a quick guide on how to setup the project for yourself


## Technologies Used
- frontend - React
- backend - Django
- database - PostgreSQL
- runtime env - Node.js
- servers - Gunicorn, nginx
- containers - Docker


## Setup
see `requirements.txt` for all dependencies. Below are the setup basics for each component.
## Django
start a new django application 
`python manage.py startapp stockosaurus`
edit the `settings.py` file accordingly
then run migrations
`python manage.py migrate`
finally, run the development server
`python manage.py runserver`

## React
create a new react app using npx
`npx create-react-app app`
navigate into app and start the application
`npm start`
The browser will open the default react app screen at `http://localhost:3000`

## Docker
the app's environment is defined with a `Dockerfile`
the app's services are defined in the `docker-compose.yml`
use the docker compose command to start and run the entire app
`docker-compose up`


## Project Status
The project is still being worked on. Looking to add functionailty to provide user options for different types of stock/crytpo analysis 


## Contact
Created by Kristian Ellis
