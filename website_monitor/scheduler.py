from apscheduler.schedulers.background import BackgroundScheduler
from utils import check_website

def start_scheduler(db):
    scheduler = BackgroundScheduler()
    for website in db.session.query(Website).all():
        scheduler.add_job(check_website, 'interval', minutes=website.frequency, args=[website])
    scheduler.start()
