import sqlalchemy as db
print(db.__version__)

engine=db.create_engine("sqlite:///Student.db")
conn=engine.connect()

metadata=db.MetaData()

Student=db.Table("student",metadata,
                 db.Column('id',db.Integer(),primary_key=True),
                 db.Column('name',db.String(20),nullable=False),
                 db.Column('branch',db.String(20),nullable=False))

metadata.create_all(engine)
