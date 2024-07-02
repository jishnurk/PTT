import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_seasons", [
    ("2 сезон 24 серия.avi", [2]),
    ("2-06. Девичья сила.mkv", [2]),
    ("2. Discovery-Kak_ustroena_Vselennaya.(2.sezon_8.serii.iz.8).2012.XviD.HDTVRip.Krasnodarka", [2]),
    ("3 сезон", [3]),
    ("3Âº Temporada Bob esponja Pt-Br", [3]),
    ("4-13 Cursed (HD).m4v", [4]),
    ("13-13-13 2013 DVDrip x264 AAC-MiLLENiUM", []),
    ("24 Season 1-8 Complete with Subtitles", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("30 M0N3D4S ESP T01XE08.mkv", [1]),
    ("Ace of the Diamond: 1st Season", [1]),
    ("Ace of the Diamond: 2nd Season", [2]),
    ("Adventure Time 10 th season", [10]),
    ("All of Us Are Dead . 2022 . S01 EP #1.2.mkv", [1]),
    ("Beavis and Butt-Head - 1a. Temporada", [1]),
    ("Boondocks, The - Seasons 1 + 2", [1, 2]),
    ("breaking.bad.s01e01.720p.bluray.x264-reward", [1]),
    ("Breaking Bad Complete Season 1 , 2 , 3, 4 ,5 ,1080p HEVC", [1, 2, 3, 4, 5]),
    ("Bron - S4 - 720P - SweSub.mp4", [4]),
    ("clny.3x11m720p.es[www.planetatorrent.com].mkv", [3]),
    ("Coupling Season 1 - 4 Complete DVDRip - x264 - MKV by RiddlerA", [1, 2, 3, 4]),
    ("DARKER THAN BLACK - S00E04 - Darker Than Black Gaiden OVA 3.mkv", [0]),
    ("Desperate.Housewives.S0615.400p.WEB-DL.Rus.Eng.avi", [6]),
    ("Desperate Housewives - Episode 1.22 - Goodbye for now.avi", [1]),
    ("Discovery. Парни с Юкона / Yokon Men [06х01-08] (2017) HDTVRip от GeneralFilm | P1", [6]),
    ("Doctor.Who.2005.8x11.Dark.Water.720p.HDTV.x264-FoV", [8]),
    ("Doctor Who S01--S07--Complete with holiday episodes", [1, 2, 3, 4, 5, 6, 7]),
    ("Dragon Ball Super S01 E23 French 1080p HDTV H264-Kesni", [1]),
    ("Dragon Ball [5.134] Preliminary Peril.mp4", [5]),
    ("Elementar 3º Temporada Dublado", [3]),
    ("Empty Nest Season 1 (1988 - 89) fiveofseven", [1]),
    ("Eu, a Patroa e as Crianças  4° Temporada Completa - HDTV - Dublado", [4]),
    ("Friends.Complete.Series.S01-S10.720p.BluRay.2CH.x265.HEVC-PSA", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ("Friends S04 Season 4 1080p 5.1Ch BluRay ReEnc-DeeJayAhmed", [4]),
    ("Futurama Season 1 2 3 4 5 6 7 + 4 Movies - threesixtyp", [1, 2, 3, 4, 5, 6, 7]),
    ("Game Of Thrones - Season 1 to 6 (Eng Subs)", [1, 2, 3, 4, 5, 6]),
    ("Game Of Thrones Complete Season 1,2,3,4,5,6,7 406p mkv + Subs", [1, 2, 3, 4, 5, 6, 7]),
    ("Game of Thrones / Сезон: 1-8 / Серии: 1-73 из 73 [2011-2019, США, BDRip 1080p] MVO (LostFilm)", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("House MD All Seasons (1-8) 720p Ultra-Compressed", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("How I Met Your Mother Season 1, 2, 3, 4, 5, & 6 + Extras DVDRip", [1, 2, 3, 4, 5, 6]),
    ("Juego de Tronos - Temp.2 [ALTA DEFINICION 720p][Cap.209][Spanish].mkv", [2]),
    ("Kyoukai no Rinne (TV) 3rd Season - 23 [1080p]", [3]),
    ("Los Simpsons Temp 7 DVDrip Espanol De Espana", [7]),
    ("Mad Men S02 Season 2 720p 5.1Ch BluRay ReEnc-DeeJayAhmed", [2]),
    ("MARATHON EPISODES/Orphan Black S3 Eps.05-08.mp4", [3]),
    ("Mash S10E01b Thats Show Biz Part 2 1080p H.264 (moviesbyrizzo upload).mp4", [10]),
    ("Merl - Temporada 1", [1]),
    ("My Little Pony - A Amizade é Mágica - T02E22.mp4", [2]),
    ("My Little Pony FiM - 6.01 - No Second Prances.mkv", [6]),
    ("Naruto Shippuden Season 1:11", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ("Once Upon a Time [S01-07] (2011-2017) WEB-DLRip by Generalfilm", [1, 2, 3, 4, 5, 6, 7]),
    ("One Punch Man 01 - 12 Season 1 Complete [720p] [Eng Subs] [Xerxe:16", [1]),
    ("Orange Is The New Black Season 5 Episodes 1-10 INCOMPLETE (LEAKED)", [5]),
    ("Otchayannie.domochozyaiki.(8.sez.21.ser.iz.23).2012.XviD.HDTVRip.avi", [8]),
    ("Perdidos: Lost: Castellano: Temporadas 1 2 3 4 5 6 (Serie Com", [1, 2, 3, 4, 5, 6]),
    ("Ranma-12-86.mp4", []),
    ("S011E16.mkv", [11]),
    ("Seinfeld S02 Season 2 720p WebRip ReEnc-DeeJayAhmed", [2]),
    ("Seinfeld Season 2 S02 720p AMZN WEBRip x265 HEVC Complete", [2]),
    ("Seizoen 22 - Zon & Maan Ultra Legendes/afl.18 Je ogen op de bal houden!.mp4", [22]),
    ("Skam.S01-S02-S03.SweSub.720p.WEB-DL.H264", [1, 2, 3]),
    ("Smallville (1x02 Metamorphosis).avi", [1]),
    ("Sons of Anarchy Sn4 Ep14 HD-TV - To Be, Act 2, By Cool Release", [4]),
    ("South Park Complete Seasons 1: 11", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    ("Stargate Atlantis ALL Seasons - S01 / S02 / S03 / S04 / S05", [1, 2, 3, 4, 5]),
    ("Stargate Atlantis Complete (Season 1 2 3 4 5) 720p HEVC x265", [1, 2, 3, 4, 5]),
    ("Teen Titans Season 1-5", [1, 2, 3, 4, 5]),
    ("Teen Wolf - 04ª Temporada 720p", [4]),
    ("The.Man.In.The.High.Castle1x01.HDTV.XviD[www.DivxTotaL.com].avi", [1]),
    ("The Boondocks Season 1, 2 & 3", [1, 2, 3]),
    ("The Boondocks Seasons 1-4 MKV", [1, 2, 3, 4]),
    ("The Expanse Complete Seasons 01 & 02 1080p", [1, 2]),
    ("The Nile Egypts Great River with Bettany Hughes Series 1 4of4 10", [1]),
    ("The Simpsons S28E21 720p HDTV x264-AVS", [28]),
    ("The Simpsons Season 20 21 22 23 24 25 26 27 - threesixtyp", [20, 21, 22, 23, 24, 25, 26, 27]),
    ("The Twilight Zone 1985 S01E22c The Library.mp4", [1]),
    ("The Twilight Zone 1985 S01E23a Shadow Play.mp4", [1]),
    ("The Walking Dead [Temporadas 1 & 2 Completas Em HDTV E Legena", [1, 2]),
    ("Tokyo Ghoul Root A - 07 [S2-07] [Eng Sub] 480p [email protected]", [2]),
    ("Travelers - Seasons 1 and 2 - Mp4 x264 AC3 1080p", [1, 2]),
    ("True Blood Season 1, 2, 3, 4, 5 & 6 + Extras BDRip TSV", [1, 2, 3, 4, 5, 6]),
    ("Vikings 3 Temporada 720p", [3]),
    ("Zvezdnie.Voiny.Voina.Klonov.3.sezon.22.seria.iz.22.XviD.HDRip.avi", [3]),
    ("[5.01] Weight Loss.avi", [5]),
    ("[Erai-raws] Granblue Fantasy The Animation Season 2 - 08 [1080p][Multiple Subtitle].mkv", [2]),
    ("[Erai-raws] Granblue Fantasy The Animation Season 2 - 10 [1080p][Multiple Subtitle].mkv", [2]),
    ("[Erai-raws] Shingeki no Kyojin Season 3 - 11 (BD 1080p Hi10 FLAC) [1FA13150].mkv", [3]),
    ("[F-D] Fairy Tail Season 1 -6 + Extras [480P][Dual-Audio]", [1, 2, 3, 4, 5, 6]),
    ("[FFA] Kiratto Pri☆chan Season 3 - 11 [1080p][HEVC].mkv", [3]),
    ("[HR] Boku no Hero Academia 87 (S4-24) [1080p HEVC Multi-Subs] HR-GZ", [4]),
    ("[SCY] Attack on Titan Season 3 - 11 (BD 1080p Hi10 FLAC) [1FA13150].mkv", [3]),
    ("Доктор Хаус 03-20.mkv", [3]),
    ("Друзья / Friends / Сезон: 1 / Серии: 1-24 из 24 [1994-1995, США, BDRip 720p] MVO + Original + Sub (Rus, Eng)", [1]),
    ("Друзья / Friends / Сезон: 1, 2 / Серии: 1-24 из 24 [1994-1999, США, BDRip 720p] MVO", [1, 2]),
    ("Интерны. Сезон №9. Серия №180.avi", [9]),
    ("Комиссар Рекс 11-13.avi", [11]),
    ("Леди Баг и Супер-Кот – Сезон 3, Эпизод 21 – Кукловод 2 [1080p].mkv", [3]),
    ("Проклятие острова ОУК_ 5-й сезон 09-я серия_ Прорыв Дэна.avi", [5]),
    ("Разрушители легенд. MythBusters. Сезон 15. Эпизод 09. Скрытая угроза (2015).avi", [15]),
    ("Сезон 5/Серия 11.mkv", [5]),
])
def test_season_detection(parser, release_name, expected_seasons):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    assert result["seasons"] == expected_seasons, f"Failed for {release_name}"