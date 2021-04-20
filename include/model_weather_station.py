from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather_station'
    id = Column(Integer, primary_key=True)
    coord_lon = Column(Float, nullable=True)
    coord_lat = Column(Float, nullable=True)
    weather_id = Column(Integer, nullable=True)
    weather_main = Column(String, nullable=True)
    weather_description = Column(String, nullable=True)
    weather_icon = Column(String, nullable=True)
    base_source = Column(String, nullable=True)
    main_temp = Column(Float, nullable=True)
    main_feels_like = Column(Float, nullable=True)
    main_temp_min = Column(Float, nullable=True)
    main_temp_max = Column(Float, nullable=True)
    main_pressure = Column(Integer, nullable=True)
    main_humidity = Column(Integer, nullable=True)
    main_sea_level = Column(Float, nullable=True)
    main_ground_level = Column(Float, nullable=True)
    visibility = Column(Integer, nullable=True)
    precipation_value = Column(Float, nullable=True)
    precipation_mode = Column(String, nullable=True)
    rain_1h = Column(Float, nullable=True)
    rain_3h = Column(Float, nullable=True)
    snow_1h = Column(Float, nullable=True)
    snow_3h = Column(Float, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_deg = Column(Float, nullable=True)
    wind_gust = Column(Float, nullable=True)
    clouds_all = Column(Float, nullable=True)
    dt = Column(Integer, nullable=True)
    sys_type = Column(Float, nullable=True)
    sys_id = Column(Float, nullable=True)
    sys_country = Column(String, nullable=True)
    sys_sunrise = Column(Date, nullable=True)
    sys_sunset = Column(Date, nullable=True)
    timezone = Column(Integer, nullable=True)
    city_id = Column(Integer, nullable=True)
    city_name = Column(String, nullable=True)
    cod = Column(Integer, nullable=True)

    def __repr__(self):
        return "<Weather(city name='{}', temp='{}', main='{}', description='{}')"\
               .format(self.city_name,
                       self.main_temp,
                       self.weather_main,
                       self.weather_description)
