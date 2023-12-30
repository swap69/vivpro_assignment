import os
import json
from django.core.management.base import BaseCommand
from app.models import Song
from vivpro_assignment import settings


class Command(BaseCommand):
    help = 'Load a list of songs from a JSON file'

    def handle(self, *args, **options):
        json_file_path = os.path.join(settings.BASE_DIR, 'app', 'playlist.json')
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for i in range(len(data['id'])):
            index = i
            song_id = data['id'][str(i)]
            song_title = data['title'][str(i)]
            danceability = data['danceability'][str(i)]
            energy = data['energy'][str(i)]
            mode = data['mode'][str(i)]
            acousticness = data['acousticness'][str(i)]
            tempo = data['tempo'][str(i)]
            duration_ms = data['duration_ms'][str(i)]
            num_sections = data['num_sections'][str(i)]
            num_segments = data['num_segments'][str(i)]

            song = Song.objects.create(index=index, id=song_id, title=song_title, danceability=danceability,
                                       energy=energy,
                                       mode=mode,
                                       acousticness=acousticness, tempo=tempo, duration_ms=duration_ms,
                                       num_sections=num_sections,
                                       num_segments=num_segments)
            song.save()
