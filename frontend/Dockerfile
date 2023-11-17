# a lightweight node image
FROM node:alpine

# working directory inside the container
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# port to expose to the outside world
EXPOSE 3001