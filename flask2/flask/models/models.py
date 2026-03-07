# models.py
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image_path = Column(String(255), nullable=True)  # ДОБАВЬТЕ ЭТО ПОЛЕ
    
    # Внешний ключ для пользователя
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # Связь с пользователем
    author = relationship("User", backref="posts")
    
    def __repr__(self):
        return f'<Post {self.title}>'