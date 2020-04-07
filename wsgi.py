from whitenoise import WhiteNoise

from api import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')