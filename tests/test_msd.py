# -*- coding: utf-8 -*-
from __future__ import absolute_import

import numpy as np
import os

import pytest

from mirdata import msd, utils
from tests.test_utils import mock_validated, mock_validator, DEFAULT_DATA_HOME
from tests.test_download_utils import mock_downloader


def test_track():
    data_home = 'tests/resources/mir_datasets/MSD'
    track = msd.Track('TRAAAFP128F931B4E3', data_home=data_home)

    with pytest.raises(ValueError):
        msd.Track('asdfasdf', data_home=data_home)

    assert track.metadata.songs[0].artist_name == 'F.L.Y. (Fast Life Yungstaz)'
    assert track.analysis.songs[0].tempo == 141.968

    assert str(track) == "msd.Track(analysis=MSDAnalysis(len(bars_start)=145, len(beats_start)=582, songs=[MSDAnalysisSong(track_id=TRAAAFP128F931B4E3, duration=246.54322, key=3, [...])], [...]), metadata=MSDMetadata(songs=[MSDMetadataSong(artist_id=ARWNWOT1242077E494, artist_name=F.L.Y. (Fast Life Yungstaz), song_id=SOYKDDB12AB017EA7A, title=Bands, [...])], artist_terms=['rap', 'def jam'], [...]), musicbrainz=MSDMusicBrainz(artist_mbtags=[], artist_mbtags_count=[], songs=[MSDMusicBrainzSong(year=0)]))"


def test_track_ids():
    data_home = 'tests/resources/mir_datasets/MSD'

    assert list(msd.track_ids(data_home=data_home)) == ['TRAAAFP128F931B4E3']
