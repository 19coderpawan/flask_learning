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


# conn.commit()

#to update the row.
update_statement=db.update(Student).where(Student.c.id==1).values(name="pawan kushwaha") #here c is the alias for column.
conn.execute(update_statement)
conn.commit()

# to select the data.
# result=conn.execute(Student.select()).fetchall()
result=conn.execute(Student.select().where(Student.c.id=="1")).fetchall() #with where clause.
for row in result:
    print(f"id={row[0]},name={row[1]},branch={row[2]}")
    # it will print out the data in console window.

# to delete the row form the table.
delete_statement=db.delete(Student).where(Student.c.id==1)
conn.execute(delete_statement)
conn.commit() 

