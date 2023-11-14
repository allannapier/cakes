# Filename: Dockerfile
FROM node:18-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN pip install -r requirements.txt
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]