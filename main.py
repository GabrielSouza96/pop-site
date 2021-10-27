import os
from popsenfermagem import app
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
    app.run(port=59000, debug=True)

