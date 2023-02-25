from flask import Blueprint, render_template
from flaskr.db import get_db

main_2 = Blueprint('main_2', __name__, url_prefix='/main_2')


@main_2.route('/names/')
def names():
    db = get_db()
    artists = db.execute(
        'SELECT DISTINCT artist FROM tracks'
    ).fetchall()
    artist_names = [row['artist'] for row in artists]
    return render_template('names.html', artists=artist_names)


@main_2.route('/tracks/')
def all_tracks():
    db = get_db()
    count = str(db.execute('SELECT COUNT(id) FROM tracks').fetchone()[0])
    return render_template('tracks.html', count=count, genre=None)


@main_2.route('/tracks/<genre>')
def tracks_by_genre(genre):
    db = get_db()
    count = str(db.execute(
        'SELECT COUNT(tracks.id) FROM tracks JOIN genres ON genres.id = tracks.genre_id WHERE genres.title = ?',
        (genre, )
    ).fetchone()[0])
    return render_template('tracks.html', count=count, genre=genre)


@main_2.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks = db.execute(
        'SELECT title, length FROM tracks'
    ).fetchall()
    return render_template('tracks_sec.html', tracks=tracks)


@main_2.route('/tracks-sec/statistics/')
def stats():
    db = get_db()
    total, avg = db.execute(
        'SELECT SUM(length), AVG(length) FROM tracks'
    ).fetchone()
    return render_template('stats.html', total=total, avg=round(avg, 2))