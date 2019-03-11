from .models import Sentences, Tags, Sentence_Tag
from django.contrib.auth.models import User


def save_word(s, w):
    Sentence_Tag.objects.create(sentence=s, tag=Tags.objects.get(id=w['tag']), word=w['name'])


def generate_tags():
    if not Tags.objects.all().count():
        data = [
            {'id': 1, 'name': 'বিশেষ্য',
             'description': 'যে পদ কোন ব্যক্তি, বস্ত্ত, প্রাণী, সমষ্টি, স্থান, কাল, ভাব, কর্ম, গুণ ইত্যাদির নাম বোঝায়, তাকে বিশেষ্য পদ বলে। প্রকারভেদ - ১. নামবাচক বা সংজ্ঞাবাচক বিশেষ্য (ক) ব্যাক্তির নাম : নজরুল, ওমর',
             'color': '#0dd1d8'},
            {'id': 2, 'name': 'বিশেষণ',
             'description': 'বিশেষণ পদ যে পদ বাক্যের অন্য কোন পদের দোষ, গুণ, অবস্থা, সংখ্যা, পরিমাণ ইত্যাদি প্রকাশ করে, তাকে বিশেষণ পদ বলে। যেমন- নীল আকাশ, সবুজ মাঠ , একটি, ভালো, দশ কেজি',
             'color': '#ffc400'},
            {'id': 3, 'name': 'সর্বনাম',
             'description': 'সর্বনাম পদ বিশেষ্য পদের পরিবর্তে যে পদ ব্যবহৃত হয়, তাকেই সর্বনাম পদ বলে। যেমন - আমি , তুমি , তোমরা, আপনি, আপনারা, সে, তারা, তাদের',
             'color': '#ff8b00'},
            {'id': 4, 'name': 'অব্যয়',
             'description': 'যে পদের কোন ব্যয় বা পরিবর্তন হয় না, তাই অব্যয় । যেমন - আর, আবার, ও, হাঁ, না, যদি, যথা, সদা, সহসা, হঠাৎ, অর্থাৎ, দৈবাৎ, বরং, পুনশ্চ, আপাতত, বস্ত্তত, আলবত, বহুত, খুব, শাবাশ, খাসা, মাইরি, মারহাবা, ও, আর, তাই, অধিকন্তু, সুতরাং, কিন্তু, বরং, তথাপি, যদ্যপি, মরি মরি!, উঃ!, ছি ছি, ওগো ,কড় কড়, ঝম ঝম, টুং টাং, কুহু কুহু, খাঁ খাঁ, টন টন ইত্যাদি',
             'color': '#66cc99'},
            {'id': 5, 'name': 'ক্রিয়া',
             'description': 'ক্রিয়া পদ যে পদ দিয়ে কোন কাজ করা বোঝায়, তাকে ক্রিয়া পদ বলে। যেমন - খাই, করি, খেলি, খেলা করা, খেলছে, দেখানো, খাওয়ানো, কনকনাচ্ছে, ফোঁসাচ্ছে, শুনে রাখ, হয়ে থাকে',
             'color': '#ff99cc'},
            {'id': 6, 'name': 'বিরাম চিহ্ন',
             'description': 'যেমন ",", "।", "?","!", "-", ":", ";", "\'", "=", "{,}", "(,)","[,]", ":-" ইত্যাদি',
             'color': '#eeee77'},
            {'id': 7, 'name': 'অসংজ্ঞায়িত',
             'description': 'চিহ্ন বা শব্দ যা পদ দ্বারা নির্নয় করা সম্ভব না',
             'color': '#ccff66'}
        ]
        for t in data:
            Tags.objects.create(**t)


def create_super_user():
    if not User.objects.all().count():
        User.objects.create_superuser(username='root', password='1', is_superuser=True, is_staff=True,
                                      email='root@posTagger.com')
