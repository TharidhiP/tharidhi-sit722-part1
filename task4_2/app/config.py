import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_week4_user:SW9n0L9IJKwk3IlLrq3pKGRuF3KbTpOp@dpg-cql18il6l47c73f17g90-a.oregon-postgres.render.com/sit722_week4")

settings = Settings()
