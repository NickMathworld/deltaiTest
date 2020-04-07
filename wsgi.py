from whitenoise import WhiteNoise

from deploy import app

application = WhiteNoise(app)
application.add_files('model/', prefix='model /')
application.add_files('utils/', prefix='utils/')
application.add_files('repositories/', prefix='repositories/')