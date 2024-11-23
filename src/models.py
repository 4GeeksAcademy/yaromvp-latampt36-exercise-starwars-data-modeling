import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=False)
    subscription_date = Column(String(250), nullable=False)

    favorite = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    user = relationship("User", back_populates="favorite")
    character = relationship("Character", back_populates="favorite")
    planet = relationship("Planet", back_populates="favorite")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    species = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    homeworld = Column(String(250), ForeignKey('planet.id'))

    planet = relationship("Planet", back_populates="character")
    favorite = relationship("Favorite", back_populates="character", single_parent=True)
    __table_args__ = (UniqueConstraint("homeworld"),)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    climate = Column(String(250))

    favorite = relationship("Favorite", back_populates="planet")
    character = relationship("Character", back_populates="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
