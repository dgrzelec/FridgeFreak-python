set -e
pytest
fastapi run fridgefreak_api/main.py --port 8000