# Use the official Nginx image as a base image
FROM nginx:alpine

# Copy Nginx configuration
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# Remove the default Nginx index.html
RUN rm -rf /usr/share/nginx/html/*

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the frontend files into the container
COPY FE /usr/share/nginx/html

# Expose port 80
EXPOSE 3000

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
