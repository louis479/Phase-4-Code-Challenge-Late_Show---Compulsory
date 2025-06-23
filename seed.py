from models import db
from models.model import Episode, Guest, Appearance
from app import create_app

app = create_app()

def seed_database():
    with app.app_context():
        print("Seeding database...")
        
        # Ensure the database is created
        db.drop_all()
        db.create_all()
        print("Database created successfully.")

        episodes = [
            Episode(date="2025-03-10", number=1),
            Episode(date="2025-03-17", number=2),
            Episode(date="2025-03-24", number=3),
            Episode(date="2025-03-31", number=4),
            Episode(date="2025-04-07", number=5)
        ]


        guests =[
            Guest(name="John Doe", occupation="Actor"),
            Guest(name="Jane Smith", occupation="Director"),
            Guest(name="Alice Johnson", occupation="Producer"),
            Guest(name="Bob Brown", occupation="Writer"),
            Guest(name="Charlie White", occupation="Musician")
        ] 

        appearances = [
            Appearance( rating=5,
                        role="Host",
                        episode=episodes[0], 
                        guest=guests [0]),
            
            Appearance( rating=4,
                        role="Guest",
                        episode=episodes[1], 
                        guest=guests[1]),

            Appearance( rating=3,
                        role="Guest",
                        episode=episodes[2], 
                        guest=guests[2]),

            Appearance( rating=2,
                        role="Guest",
                        episode=episodes[3], 
                        guest=guests[3]),

            Appearance( rating=1,
                        role="Guest",
                        episode=episodes[4], 
                        guest=guests[4])
        ]

        db.session.add_all(episodes)
        db.session.add_all(guests)
        db.session.add_all(appearances)

        try:
            db.session.commit()
            print("Data seeded successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding data: {e}")

if __name__ == "__main__":
    seed_database()
#     print("Database seeding complete.")
#     app.run(debug=True)

        