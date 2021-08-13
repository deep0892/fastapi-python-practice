Create virtual environment:
python -m env blog-env

Activate virtual environment:
source blog-env/bin/activate

Install dependencies from requirement.txt:
pip install -r requirements.txt

Run the application in development:
uvicorn blog.main:app --reload

