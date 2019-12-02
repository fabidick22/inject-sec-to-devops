#!/usr/bin/env python3

import os
from app import create_app
from pathlib import Path  
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = create_app(os.getenv('FLASK_ENV'))

if __name__ == "__main__":
    app.run()
