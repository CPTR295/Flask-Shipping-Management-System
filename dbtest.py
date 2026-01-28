from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import text 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Trace%40Postgres235@localhost:5432/smsdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    try:
        # ✅ SQLAlchemy 2.0+ syntax
        with db.engine.connect() as conn:
           
            result = conn.execute(text("SELECT version();"))
            print("✅ CONNECTION OK!")

    except Exception as e:
        print(f"❌ CONNECTION FAILED: {e}")