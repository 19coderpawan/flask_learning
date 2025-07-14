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

# lets insert the data in the table.
# insert_statement=db.insert(Student).values(id=1,name="pawan",branch="mca")
# result=conn.execute(insert_statement)

# to select the data.
# result=conn.execute(Student.select()).fetchall()
result=conn.execute(Student.select().where(Student.c.name=="pawan")).fetchall() #with where clause.
for row in result:
    print(f"id={row[0]},name={row[1]},branch={row[2]}")
    # it will print out the data in console window.
# conn.commit()
