import os


def on_start(path):
    
    open('__init__.py', 'w')
    
    os.chdir(path)
    
def version1(apath):
    
    ver = 'version1'
    vpath = os.path.join(apath, ver)
    os.mkdir(vpath)
    os.chdir(vpath)
    
    on_start(apath)
    
def models(dpath):
        
    model = 'models'
    mpath = os.path.join(dpath, model)
    os.mkdir(mpath)
    os.chdir(mpath)
        
    on_start(dpath)
    
    
    
def schemas():
    
    schemas = 'schemas' # creating schema dir 
    spath = os.path.join(create_app.parent, schemas)
    os.mkdir(spath)
    print("schemas folder created...")
    os.chdir(spath)
    
    on_start(create_app.parent)
    
def static():
    
    static = 'static'
    spath = os.path.join(create_app.parent, static)
    os.mkdir(spath)
    print("static folder created... store your media files here")
    
def templates():
    
    temp = 'templates'
    tpath = os.path.join(create_app.parent, temp)
    os.mkdir(tpath)
    print("templates folder created... write your html files here.")
    
def tests():
    
    test = 'tests'
    zpath = os.path.join(create_app.parent, test)
    os.mkdir(zpath)
    print("tests folder created...")
    os.chdir(zpath)
    
    on_start(create_app.parent)
    
    
def apis():
    
    apis = 'apis'
    apath = os.path.join(create_app.parent, apis)
    os.mkdir(apath)
    print("apis folder created ... write your api routers here.")
    os.chdir(apath)
    
    version1(apath)
    
    base = open('base.py', 'w')
    base.write(" # The base file is a collection of all your api routers.")
    base.close()
    
    on_start(create_app.parent)
    
    
def core():
    
    core = 'core'
    cpath = os.path.join(create_app.parent, core)
    os.mkdir(cpath)
    print("core folder created... update security files here")
    os.chdir(cpath)
    
    file = open('config.py', 'w')
    file.write(" # Here you can write your configuration files")
    file.close()
    
    hash = open('hashing.py', 'w')
    hash.write(
    """
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    """
    )
    hash.close()
    
    secure = open('security.py', 'w')
    secure.write(
    """
from datetime import datetime  
from datetime import timedelta
from typing import Optional
from jose import jwt


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES  
        )
    to_encode.update({"exp": expire})               
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM 
    )
    return encoded_jwt

    """
    )
    
    secure.close()
    
    on_start(create_app.parent)
    
    
def db():
    
    database = 'db'
    dpath = os.path.join(create_app.parent, database)
    os.mkdir(dpath)
    print("database file created...")
    os.chdir(dpath)
    sess = open('session.py', 'w')
    sess.write(
    """
from sqlalchemy import create_engine # Don't worry, i done this work for you :)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
    """
    )
    sess.close()
    
    models(dpath)
        
    on_start(create_app.parent)
        

def create_app(dir):
    
    create_app.parent = dir
    
    os.chdir(create_app.parent)
    
    open('main.py', 'w')
        
    print("main file created...")
    
    schemas()
    db()
    core()
    apis()
    static()
    templates()
    tests()
    

    
    
    
    