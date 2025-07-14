# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the /app folder in container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "pipeline.py"]

