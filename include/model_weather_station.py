from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather_station'
    id = Column(Integer, primary_key=True)
    coord_lon = Column(Float)
    coord_lat = Column(Float)
    weather_id = Column(Integer)
    weather_main = Column(String)
    weather_description = Column(String)
    weather_icon = Column(String)
    base_source = Column(String)
    main_temp = Column(Float)
    main_feels_like = Column(Float)
    main_temp_min = Column(Float)
    main_temp_max = Column(Float)
    main_pressure = Column(Integer)
    main_humidity = Column(Integer)
    main_sea_level = Column(Float)
    main_ground_level = Column(Float)
    visibility = Column(Integer)
    precipation_value = Column(Float)
    precipation_mode = Column(String)
    wind_speed = Column(Float)
    wind_deg = Column(Float)
    wind_gust = Column(Float)
    clouds_all = Column(Float)
    dt = Column(Date)
    sys_type = Column(Float)
    sys_id = Column(Float)
    sys_country = Column(String)
    sys_sunrise = Column(Date)
    sys_sunset = Column(Date)
    timezone = Column(Integer)
    id = Column(Integer)
    name = Column(String)
    cod = Column(Integer)

    def __repr__(self):
        return "<Weather(name='{}', temp='{}', main='{}', description='{}')"\
               .format(self.name,
                       self.main_temp,
                       self.weather_main,
                       self.weather_description)
