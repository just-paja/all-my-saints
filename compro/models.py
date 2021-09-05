from django.db.models import (DateTimeField, DecimalField, ForeignKey,
                              CharField, FileField, ImageField, IntegerField,
                              Model, TextField, RESTRICT, CASCADE)


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(BaseModel):
    name = CharField(max_length=63)

    def __str__(self):
        return 'Team %s' % self.name


class TeamMember(BaseModel):
    name = CharField(max_length=255)
    team = ForeignKey(Team, related_name='members', on_delete=CASCADE)

    def __str__(self):
        return '%s [%s]' % (self.name, self.team)


class Indulgence(BaseModel):
    team = ForeignKey(Team, related_name='indulgences', on_delete=CASCADE)
    value = IntegerField(default=1)
    comment = TextField(null=True, blank=True)


class Compro(BaseModel):
    title = CharField(max_length=255)
    text = TextField(null=True)
    lat = DecimalField(null=True, decimal_places=9, max_digits=12)
    lng = DecimalField(null=True, decimal_places=9, max_digits=12)
    team = ForeignKey(
        Team,
        related_name='compro_items',
        on_delete=RESTRICT,
    )

    def __str__(self):
        return 'Compro: %s' % self.title


class ComproMedia(BaseModel):
    image = ImageField(upload_to='compro/photos')
    video = FileField(upload_to='compro/videos')
    compro = ForeignKey(
        Compro,
        related_name='media',
        on_delete=RESTRICT,
    )
