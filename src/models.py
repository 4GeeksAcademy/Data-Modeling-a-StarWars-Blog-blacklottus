from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, foreign

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(70), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    username: Mapped[str] = mapped_column(String(70), unique=True, nullable=False)

    favorites = relationship("Favorites", back_populates="user")


class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="favorites")
    # Add these if Favorites can store Characters or Planets
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=True)

    character = relationship("Characters", backref="favorites")
    planet = relationship("Planets", backref="favorites")


class Characters(db.Model):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), nullable=False)
    age: Mapped[str] = mapped_column(String(70), nullable=True)
    homeworld: Mapped[str] = mapped_column(String(70), nullable=True)

    # Optional: relationship if you want to access the planet from a character
    # Note: This assumes Planets.name is unique
    planet = relationship("Planets", primaryjoin="foreign(Characters.homeworld) == Planets.name", back_populates="residents")


class Planets(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), unique=True, nullable=False)

    residents = relationship("Characters", primaryjoin="foreign(Characters.homeworld) == Planets.name", back_populates="planet")
