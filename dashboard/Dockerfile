# Use an official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the dashboard code
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Start the Streamlit dashboard
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
