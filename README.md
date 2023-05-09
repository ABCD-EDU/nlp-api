# API for NLP Project

This API is used by our NLP project's proof of concept and contains the endpoints to process LDA and Sentiment analysis tasks for our application.

## Development

To set up the project for development, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download BERTopic model

   ```
   curl -o "app\loaders\model\topic\topic_model_mmr" https://drive.google.com/file/d/1gTi21FE35IEfSEWhLgE9dv5KBAQf8Qj0/view?usp=share_link
   ```

5. Start the server:

   ```
   uvicorn main:app --reload
   ```

6. Navigate to `http://localhost:8000/docs` in your web browser to view the API documentation.
