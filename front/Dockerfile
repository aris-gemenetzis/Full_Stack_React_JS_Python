# Use the latest LTS version of Node.js
FROM node:13
 
# Set the working directory inside the container
WORKDIR /front
 
# Copy package.json and package-lock.json
COPY package*.json ./
 
# Install dependencies
RUN npm install
 
# Copy application files
COPY . .
 
# Expose port to run the app
EXPOSE 3000
 
# Define the command to run your app
CMD ["npm", "start"]