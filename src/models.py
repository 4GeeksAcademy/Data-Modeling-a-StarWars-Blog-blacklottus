from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

# Inicializar SQLAlchemy
db = SQLAlchemy()

# Tablas intermedias para relaciones muchos-a-muchos

people_films = Table(
    'people_films', db.Model.metadata,
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True)
)

people_starships = Table(
    'people_starships', db.Model.metadata,
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'), primary_key=True)
)

people_vehicles = Table(
    'people_vehicles', db.Model.metadata,
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)
)

people_species = Table(
    'people_species', db.Model.metadata,
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True),
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'), primary_key=True)
)

planet_films = Table(
    'planet_films', db.Model.metadata,
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True)
)

film_species = Table(
    'film_species', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'), primary_key=True)
)

film_starships = Table(
    'film_starships', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'), primary_key=True)
)

film_vehicles = Table(
    'film_vehicles', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)
)

# Modelos principales

class People(db.Model):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    birth_year: Mapped[str] = mapped_column(String, nullable=False)
    eye_color: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    hair_color: Mapped[str] = mapped_column(String, nullable=False)
    height: Mapped[str] = mapped_column(String, nullable=False)
    mass: Mapped[str] = mapped_column(String, nullable=False)
    skin_color: Mapped[str] = mapped_column(String, nullable=False)
    homeworld: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    edited: Mapped[str] = mapped_column(String, nullable=False)

    films = relationship("Films", secondary=people_films, back_populates="characters")
    starships = relationship("Starships", secondary=people_starships, back_populates="pilots")
    vehicles = relationship("Vehicles", secondary=people_vehicles, back_populates="pilots")
    species = relationship("Species", secondary=people_species, back_populates="people")


class Films(db.Model):
    __tablename__ = 'films'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    episode_id: Mapped[int] = mapped_column(Integer, nullable=False)
    opening_crawl: Mapped[str] = mapped_column(String)
    director: Mapped[str] = mapped_column(String)
    producer: Mapped[str] = mapped_column(String)
    release_date: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    edited: Mapped[str] = mapped_column(String)

    characters = relationship("People", secondary=people_films, back_populates="films")
    planets = relationship("Planets", secondary=planet_films, back_populates="films")
    species = relationship("Species", secondary=film_species, back_populates="films")
    starships = relationship("Starships", secondary=film_starships, back_populates="films")
    vehicles = relationship("Vehicles", secondary=film_vehicles, back_populates="films")


class Starships(db.Model):
    __tablename__ = 'starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    starship_class: Mapped[str] = mapped_column(String)
    manufacturer: Mapped[str] = mapped_column(String)
    cost_in_credits: Mapped[str] = mapped_column(String)
    length: Mapped[str] = mapped_column(String)
    crew: Mapped[str] = mapped_column(String)
    passengers: Mapped[str] = mapped_column(String)
    max_atmosphering_speed: Mapped[str] = mapped_column(String)
    hyperdrive_rating: Mapped[str] = mapped_column(String)
    MGLT: Mapped[str] = mapped_column(String)
    cargo_capacity: Mapped[str] = mapped_column(String)
    consumables: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    edited: Mapped[str] = mapped_column(String)

    pilots = relationship("People", secondary=people_starships, back_populates="starships")
    films = relationship("Films", secondary=film_starships, back_populates="starships")


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    vehicle_class: Mapped[str] = mapped_column(String)
    manufacturer: Mapped[str] = mapped_column(String)
    length: Mapped[str] = mapped_column(String)
    cost_in_credits: Mapped[str] = mapped_column(String)
    crew: Mapped[str] = mapped_column(String)
    passengers: Mapped[str] = mapped_column(String)
    max_atmosphering_speed: Mapped[str] = mapped_column(String)
    cargo_capacity: Mapped[str] = mapped_column(String)
    consumables: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    edited: Mapped[str] = mapped_column(String)

    pilots = relationship("People", secondary=people_vehicles, back_populates="vehicles")
    films = relationship("Films", secondary=film_vehicles, back_populates="vehicles")


class Species(db.Model):
    __tablename__ = 'species'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    classification: Mapped[str] = mapped_column(String)
    designation: Mapped[str] = mapped_column(String)
    average_height: Mapped[str] = mapped_column(String)
    average_lifespan: Mapped[str] = mapped_column(String)
    eye_colors: Mapped[str] = mapped_column(String)
    hair_colors: Mapped[str] = mapped_column(String)
    skin_colors: Mapped[str] = mapped_column(String)
    language: Mapped[str] = mapped_column(String)
    homeworld: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    edited: Mapped[str] = mapped_column(String)

    people = relationship("People", secondary=people_species, back_populates="species")
    films = relationship("Films", secondary=film_species, back_populates="species")


class Planets(db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    diameter: Mapped[str] = mapped_column(String)
    rotation_period: Mapped[str] = mapped_column(String)
    orbital_period: Mapped[str] = mapped_column(String)
    gravity: Mapped[str] = mapped_column(String)
    population: Mapped[str] = mapped_column(String)
    climate: Mapped[str] = mapped_column(String)
    terrain: Mapped[str] = mapped_column(String)
    surface_water: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    edited: Mapped[str] = mapped_column(String)

    films = relationship("Films", secondary=planet_films, back_populates="planets")
    residents = relationship("People", primaryjoin="Planets.name == foreign(People.homeworld)")
