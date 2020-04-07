news = {
    'type': 'object',
    'properties': {
        'keywords': {'type': 'array','items':{'type':'string'} },
        'language': {'type': 'string'},
    },
    'required': ['keywords','language']
}