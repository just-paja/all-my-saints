from django.db.models import (DateTimeField, DecimalField, ForeignKey,
                              CharField, FileField, ImageField, Model,
                              TextField, RESTRICT, CASCADE)


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(BaseModel):
    name = CharField(max_length=63)


class TeamMember(BaseModel):
    name = CharField(max_length=255)
    team = ForeignKey(Team, related_name='members', on_delete=CASCADE)


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


class ComproMedia(BaseModel):
    image = ImageField(upload_to='compro/photos')
    video = FileField(upload_to='compro/videos')
    compro = ForeignKey(
        Compro,
        related_name='media',
        on_delete=RESTRICT,
    )
