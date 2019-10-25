from typing import List

import lyricsgenius
from flask import current_app

from src.exception.error import UnexpectedError
from src.usecases.music.dto.search_lyric_request import SearchLyricRequest
from src.usecases.music.dto.search_lyric_response import SearchLyricResponse
from src.usecases.music.search_lyric_usecase import SearchLyricUseCase


class SearchLyricInteractor(SearchLyricUseCase):

    def __init__(self):
        self._genius = lyricsgenius.Genius(current_app.config['GENIUS_TOKEN'])
        self._genius.verbose = False
        self._genius.remove_section_headers = True
        self._genius.skip_non_songs = False
        self._genius.excluded_terms = ["(Remix)", "(Live)"]

    def search_by_artist_song(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        song = self._genius.search_song(request.song, request.artist)

        if not song:
            raise UnexpectedError(f"Not found {request.song}.")

        return [
            SearchLyricResponse(song.artist, song.title, song.song_art_image_url, song.lyrics)
        ]

    def search_by_artist(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        artist = self._genius.search_artist(request.artist, max_songs=4, get_full_info=False)

        if not artist:
            raise UnexpectedError(f"Not found songs of {artist}.")

        return [
            SearchLyricResponse(song.artist, song.title, song.song_art_image_url, song.lyrics) for song in artist.songs
        ]

    def search_by_song(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        song = self._genius.search_song(request.song, get_full_info=False)

        if not song:
            raise UnexpectedError(f"Not found {request.song}.")

        return [
            SearchLyricResponse(song.artist, song.title, song.song_art_image_url, song.lyrics)
        ]