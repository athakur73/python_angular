from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
from sqlalchemy.orm.attributes import QueryableAttribute

#db_url = 'localhost:5432'
#db_name = 'online-exam'
#db_user = 'postgres'
#db_password = '0NLIN3-ex4m'
#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
engine = create_engine("mssql+pyodbc://localhost\SQLEXPRESS/master?driver=SQL Server?Trusted_Connection=yes")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class authUser(Base):
    __tablename__ = 'authUser'
    id = Column(Integer, primary_key=True)
    emp_id = Column(String)
    username = Column(String)
    password = Column(String)
    
class employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    emp_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    sur_name = Column(String)
    initial = Column(String) 
    salutation = Column(String) #mr,ms, Miss, Mrs
    project_code = Column(String)
    dept = Column(String)

    emp_start_date = Column(DateTime)
    emp_last_working_date = Column(DateTime)
    emp_project_assigned_date = Column(DateTime)
    emp_project_end_date = Column(DateTime)

    employment_status = Column(String) #in project, new joined, in notice, bench, relieved
    manager_name = Column(String) 
    manager_dept = Column(String)
    resource_status = Column(String)
    delivery_type = Column(String)
    additional_allocation =  Column(String)
    skills =  Column(String)
    roles =  Column(String)
    # def __init__(self, created_by):
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     self.last_updated_by = created_by

    
    def to_dict(self, show=None, _hide=[], _path=None):
        """Return a dictionary representation of this model."""

        show = show or []

        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []
        default = self._default_fields if hasattr(self, "_default_fields") else []
        default.extend(['id', 'modified_at', 'created_at'])

        if not _path:
            _path = self.__tablename__.lower()

            def prepend_path(item):
                item = item.lower()
                if item.split(".", 1)[0] == _path:
                    return item
                if len(item) == 0:
                    return item
                if item[0] != ".":
                    item = ".%s" % item
                item = "%s%s" % (_path, item)
                return item

            _hide[:] = [prepend_path(x) for x in _hide]
            show[:] = [prepend_path(x) for x in show]

        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()
        properties = dir(self)

        ret_data = {}

        for key in columns:
            if key.startswith("_"):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                ret_data[key] = getattr(self, key)

        for key in relationships:
            if key.startswith("_"):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                _hide.append(check)
                is_list = self.__mapper__.relationships[key].uselist
                if is_list:
                    items = getattr(self, key)
                    if self.__mapper__.relationships[key].query_class is not None:
                        if hasattr(items, "all"):
                            items = items.all()
                    ret_data[key] = []
                    for item in items:
                        ret_data[key].append(
                            item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        )
                else:
                    if (
                        self.__mapper__.relationships[key].query_class is not None
                        or self.__mapper__.relationships[key].instrument_class
                        is not None
                    ):
                        item = getattr(self, key)
                        if item is not None:
                            ret_data[key] = item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        else:
                            ret_data[key] = None
                    else:
                        ret_data[key] = getattr(self, key)

        for key in list(set(properties) - set(columns) - set(relationships)):
            if key.startswith("_"):
                continue
            if not hasattr(self.__class__, key):
                continue
            attr = getattr(self.__class__, key)
            if not (isinstance(attr, property) or isinstance(attr, QueryableAttribute)):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                val = getattr(self, key)
                if hasattr(val, "to_dict"):
                    ret_data[key] = val.to_dict(
                        show=list(show),
                        _hide=list(_hide), _path=("%s.%s" % (_path, key.lower()))
                        #_path=('%s.%s' % (path, key.lower())),
                    )
                else:
                    try:
                        ret_data[key] = json.loads(json.dumps(val))
                    except:
                        pass

        return ret_data

class project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    project_code = Column(String)
    project_name = Column(String)
    project_start_date = Column(DateTime)
    project_status = Column(String)
    billing_type = Column(String)
    segment = Column(String)
    geography = Column(String)
    solution_category = Column(String)
    financial_year = Column(String)

    def to_dict(self, show=None, _hide=[], _path=None):
        """Return a dictionary representation of this model."""

        show = show or []

        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []
        default = self._default_fields if hasattr(self, "_default_fields") else []
        default.extend(['id', 'modified_at', 'created_at'])

        if not _path:
            _path = self.__tablename__.lower()

            def prepend_path(item):
                item = item.lower()
                if item.split(".", 1)[0] == _path:
                    return item
                if len(item) == 0:
                    return item
                if item[0] != ".":
                    item = ".%s" % item
                item = "%s%s" % (_path, item)
                return item

            _hide[:] = [prepend_path(x) for x in _hide]
            show[:] = [prepend_path(x) for x in show]

        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()
        properties = dir(self)

        ret_data = {}

        for key in columns:
            if key.startswith("_"):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                ret_data[key] = getattr(self, key)

        for key in relationships:
            if key.startswith("_"):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                _hide.append(check)
                is_list = self.__mapper__.relationships[key].uselist
                if is_list:
                    items = getattr(self, key)
                    if self.__mapper__.relationships[key].query_class is not None:
                        if hasattr(items, "all"):
                            items = items.all()
                    ret_data[key] = []
                    for item in items:
                        ret_data[key].append(
                            item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        )
                else:
                    if (
                        self.__mapper__.relationships[key].query_class is not None
                        or self.__mapper__.relationships[key].instrument_class
                        is not None
                    ):
                        item = getattr(self, key)
                        if item is not None:
                            ret_data[key] = item.to_dict(
                                show=list(show),
                                _hide=list(_hide),
                                _path=("%s.%s" % (_path, key.lower())),
                            )
                        else:
                            ret_data[key] = None
                    else:
                        ret_data[key] = getattr(self, key)

        for key in list(set(properties) - set(columns) - set(relationships)):
            if key.startswith("_"):
                continue
            if not hasattr(self.__class__, key):
                continue
            attr = getattr(self.__class__, key)
            if not (isinstance(attr, property) or isinstance(attr, QueryableAttribute)):
                continue
            check = "%s.%s" % (_path, key)
            if check in _hide or key in hidden:
                continue
            if check in show or key in default:
                val = getattr(self, key)
                if hasattr(val, "to_dict"):
                    ret_data[key] = val.to_dict(
                        show=list(show),
                        _hide=list(_hide), _path=("%s.%s" % (_path, key.lower()))
                        #_path=('%s.%s' % (path, key.lower())),
                    )
                else:
                    try:
                        ret_data[key] = json.loads(json.dumps(val))
                    except:
                        pass

        return ret_data
    #serialize_only = ('id', 'email_id', 'role_type', 'users.id')
    # _default_fields = [
    #     "title",
    #     "description",
    # ]
    # _hidden_fields = []
    # _readonly_fields = []

    # def __init__(self, title, description, created_by):
    #     Entity.__init__(self, created_by)
    #     self.title = title
    #     self.description = description
def serialize_all(data_obj):
    serialized = []
    for data in data_obj:
        data_dict = data.__dict__
        #print(data_dict)
    
        data_dict_keys = list(data_dict.keys())
        #print(data_dict_keys)
        #print(type(data_dict_keys))

        serial_dict ={}
        for i in range(1,len(data_dict_keys)):
            serial_dict[data_dict_keys[i]]=data_dict[data_dict_keys[i]]
        serialized.append(serial_dict)
    return serialized 
    