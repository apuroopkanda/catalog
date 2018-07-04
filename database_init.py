from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create sample users
User1 = User(name="Apuroop Kanda",
             email="apuroop3@gmail.com",
             picture='https://lh3.googleusercontent.com/-swHhvZC8wYw/AAAAAAAAAAI/AAAAAAAAFoo/ElNgF4R0Shw/s120-p-rw-no/photo.jpg')
session.add(User1)
session.commit()


# Create sample categories
Category1 = Category(name="Car & Motor Bikes",
                     user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Gadgets",
                     user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Clothing",
                     user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Apps & Games",
                     user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Music",
                     user_id=1)
session.add(Category5)
session.commit()


# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Mobile",
              date=datetime.datetime.now(),
              description="2 GB RAM | 32 GB ROM "
              "  4.7 inch Full HD+ Display 12MP Rear Camera"
              " | 7MP Front Camera 1960 mAh Li Polymer Battery"
              " Quad-core 2.34 GHz Processor with Apple A10 Fusion chipset",
              picture="https://cdn.shopify.com/s/files/1/1316/3851/products/iphone-7-jet-black-05_1024x1024.jpg?v=1484648678",
              category_id=2,
              user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="United Colors of Benetton Men's Casual Shirt",
              date=datetime.datetime.now(),
              description="Cut to offer maximum stretch during sultry summer days is this dark grey casual shirt from United Colors of Benetton. Highlighted with a textured woven design and contrast piping on collar, this full-sleeved shirt is a wardrobe must-have. Made from cotton spandex fabric, this shirt is comfortable to wear with denims and lace-ups.",
              picture="https://images-eu.ssl-images-amazon.com/images/I/414roJF5UPL._AC_UL260_SR200,260_FMwebp_QL70_.jpg",
              category_id=3,
              user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Honda City",
              date=datetime.datetime.now(),
              description="The Honda City is a compact car which has been produced by the Japanese manufacturer Honda since 1981.",
              picture="https://img.gaadicdn.com/images/car-images/large/Honda/Honda-City/Tefeta-white.jpg",
              category_id=1,
              user_id=1)
session.add(Item3)
session.commit()

print("Your database has been populated with sample data!")
