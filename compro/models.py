from django.urls import reverse
from django.db.models import (DateTimeField, DecimalField, ForeignKey,
                              CharField, FileField, ImageField, IntegerField,
                              Model, SlugField, TextField, RESTRICT, CASCADE)


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


class Documentation(BaseModel):
    title = CharField(max_length=255)
    text = TextField(null=True)
    team = ForeignKey(
        Team,
        related_name='documentation_items',
        on_delete=RESTRICT,
    )

    def __str__(self):
        return 'Documentation: %s' % self.title


class HollyCompro(BaseModel):
    title = CharField(max_length=255)
    slug = SlugField()
    text = TextField(null=True, blank=True)
    lat = DecimalField(blank=True, null=True, decimal_places=9, max_digits=12)
    lng = DecimalField(blank=True, null=True, decimal_places=9, max_digits=12)
    value = IntegerField(default=1)

    def get_absolute_url(self):
        return reverse('compro_detail', kwargs={"compro_slug": self.slug})


class HollyComproAcquisition(BaseModel):
    team = ForeignKey(Team,
                      related_name='compro_acquisitions',
                      on_delete=CASCADE)
    compro = ForeignKey(HollyCompro,
                        related_name='acquisitions',
                        on_delete=RESTRICT)


class DocumentationMedia(BaseModel):
    image = ImageField(upload_to='documentation/photos')
    video = FileField(upload_to='documentation/videos')
    documentation = ForeignKey(
        Documentation,
        related_name='media',
        on_delete=RESTRICT,
    )
