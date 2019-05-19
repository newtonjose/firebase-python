from jsonmodels import models, fields, errors, validators


class GitRepo(models.Base):
    name = fields.StringField(required=True)
    language = fields.StringField(required=True)
    stars = fields.IntField()


class GitUser(models.Base):
    name = fields.StringField(required=True)
    nickname = fields.StringField(required=True)
    repos = fields.ListField([GitRepo,], nullable=True)
    

class City(models.Base):
    name = fields.StringField(required=True)
    state = fields.StringField()
    country = fields.StringField(required=True)
    capital = fields.BoolField(nullable=True)
    population = fields.IntField(nullable=True)
    
    def __repr__(self):
        return u'City(name={}, country={}, population={}, capital={})'.format(
           self.name, self.country, self.population, self.capital)

    
