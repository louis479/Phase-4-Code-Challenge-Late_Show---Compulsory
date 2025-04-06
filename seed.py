from app import db, Episode, Guest, Appearance

episode = Episode(date="2025-03-10", number=1)
guest = Guest(name="John Doe", occupation="Actor")

appearance = Appearance(rating=5, episode=episode, guest=guest)

db.session.add(episode)
db.session.add(guest)
db.session.add(appearance)
db.session.commit()

print("Data seeded successfully!")