from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from configs.db_connection import Base

class Collar(Base):
    __tablename__ = "collars"

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, nullable=True)
    tag = Column(String, unique=True, nullable=False)
    status = Column(Boolean, nullable=False, server_default=text("FALSE"))
    available_balance = Column(Numeric(10, 2))
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

