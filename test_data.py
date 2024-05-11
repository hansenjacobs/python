person_schema = {
    'title': 'person',
    'properties': {
        'name': {
            'type': dict,
            'properties': {
                'first': {
                    'type': str,
                    'length-min': 1,
                    'length-max': 100,
                    'required': True,
                },
                'middle': {
                    'type': str,
                    'length-min': 1,
                    'length-max': 100,
                    'required': False,
                },
                'first': {
                    'type': str,
                    'length-min': 1,
                    'length-max': 100,
                    'required': True,
                },
            }
        },
        'date_of_birth': {
            'type': str,
            'length-min': 10,
            'length-max': 10,
            'required': True,
        },
        'email_addresses': {
            'type': list,
            'items': {
                'type': str,
                'length-min': 6,
                'length-max': 256
            },
            'length-min': 1,
        },
        'addresses': {
            'type': list,
            'items': {
                'type': dict,
                'properties': {
                    'address_line_1': {
                        'type': str,
                        'length-max': 256,
                        'required': True,
                    },
                    'address_line_2': {
                        'type': str,
                        'length-max': 256,
                        'required': False,
                    },
                    'city': {
                        'type': str,
                        'length-max': 256,
                        'required': True,
                    },
                    'state': {
                        'type': str,
                        'length-max': 2,
                        'required': True,
                    },
                    'zip': {
                        'type': str,
                        'length-max': 10,
                        'required': True,
                    },
                }
            },
            'length-min': 1,
        }
    }
}

person_1 = {
    'name': {
        'first': 'Jacob',
        'middle': 'S',
        'last': 'Hansen'
    },
    'email_addresses': [
        'hansenjacobs@gmail.com',
        'thejakesquared@gmail.com',
    ],
    'date_of_birth': '1989-03-24',
    'addresses': [
        {
            'address_line_1': '3402 Concord Ave',
            'city': 'Madison',
            'state': 'WI',
            'zip': '53714',
        },
    ]
}

person_2 = {
    'name': {
        'first': 'Jacob',
        'last': 'Hansen'
    },
    'email_addresses': [
        'jakebcrouse@gmail.com'
    ],
    'date_of_birth': 19870912,
    'addresses': [
        {
            'address_line_1': '3402 Concord Ave',
            'address_line_2': 2,
            'city': 'Madison',
            'state': 'WI',
            'zip': '53714',
        },
    ]
}
