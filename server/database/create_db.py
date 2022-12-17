from server.database.database import base, engine


base.metadata.create_all(engine)
print("Create the database")
