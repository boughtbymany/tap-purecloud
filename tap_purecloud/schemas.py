historical_adherence = {
    'type': 'object',
    'properties': {
        "userId": {
            "type": ["null", "string"]
        },
        "startDate": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "endDate": {
            "type": ["null", "string"],
            "format": "date-time"
        },
        "impact": {
            "type": ["null", "string"]
        },
        "exceptionInfo": {
            "type": ["null", "array"],
            "items": {
                "type": ["object", "null"]
            }
        },
        "management_unit_id": {
            "type": ["null", "string"]
        },
        "dayMetrics": {
            "type": ["null", "array"],
            "items": {
                "type": ["null", "object"],
                "properties": {
                    "dayStartOffsetSecs": {
                        "type": ["null", "number"]
                    },
                    "adherenceScheduleSecs": {
                        "type": ["null", "number"]
                    },
                    "conformanceScheduleSecs": {
                        "type": ["null", "number"]
                    },
                    "conformanceActualSecs": {
                        "type": ["null", "number"]
                    },
                    "exceptionCount": {
                        "type": ["null", "number"]
                    },
                    "exceptionDurationSecs": {
                        "type": ["null", "number"]
                    },
                    "impactSeconds": {
                        "type": ["null", "number"]
                    },
                    "scheduleLengthSecs": {
                        "type": ["null", "number"]
                    },
                    "actualLengthSecs": {
                        "type": ["null", "number"]
                    }
                }
            }
        }
    }
}

user = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'description': 'email for the user',
        },
        'id': {
            'type': 'string',
            'description': 'id for the user',
        },
        'name': {
            'type': 'string',
            'description': 'name for the user',
        },
        'username': {
            'type': 'string',
            'description': 'username for the user',
        },
        'division': {
            'type': ['object', 'null'],
            'properties': {
                'id': {
                    'type': ['null', 'string'],
                    'description': 'user division'
                }
            }
        }
    }
}

group = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'description': 'name for the group',
        },
        'id': {
            'type': 'string',
            'description': 'id for the group',
        },
        'state': {
            'type': 'string',
            'description': 'state for the group',
        },
        'visibility': {
            'type': 'string',
            'description': 'visibility for the group',
        }
    }
}

location = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the location',
        },
        'name': {
            'type': 'string',
            'description': 'name for the location',
        },
        'state': {
            'type': 'string',
            'description': 'state for the location',
        }
    }
}


segment = {
    'type': 'object',
    'properties': {
        'queue_id': {
            'type': ['string', 'null'],
            'description': 'id for the queue',
        },
        'source_session_id': {
            'type': ['string', 'null'],
            'description': 'id for the session',
        },
        'segment_start': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'start datetime for the segment',
        },
        'segment_end': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'end datetime for the segment',
        },
        'wrap_up_code': {
            'type': ['string', 'null'],
            'description': 'wrap up code'
        },
        'segment_type': {
            'type': ['string', 'null'],
            'description': 'segment type'
        },
        'disconnect_type': {
            'type': ['string', 'null'],
            'description': 'disconnect type'
        }
    }
}

metrics = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'description': 'Metrics name'
        },
        'value': {
            'type': 'number',
            'description': 'metric value'
        },
        'emit_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'metric emit date'
        }
    }
}


session = {
    'type': 'object',
    'properties': {
        'session_id': {
            'type': 'string',
            'description': 'id for the session',
        },
        'media_type': {
            'type': ['string', 'null'],
            'description': 'media type name'
        },
        'ani': {
            'type': ['string', 'null'],
            'description': 'ani value'
        },
        'direction': {
            'type': ['string', 'null'],
            'description': 'direction'
        },
        'dnis': {
            'type': ['string', 'null'],
            'description': 'DNIS'
        },
        'outbound_campaign_id': {
            'type': ['string', 'null'],
            'description': 'Outbound campaign id',
        },
        'outbound_contact_id': {
            'type': ['string', 'null'],
            'description': 'Outbound contact id',
        },
        'recording': {
            'type': ['boolean', 'null'],
            'description': 'Recording'
        },
        'segments': {
            'type': ['array', 'null'],
            'items': segment
        },
        'metrics': {
            'type': ['array', 'null'],
            'items': metrics
        }
    }
}


participant = {
    'type': 'object',
    'properties': {
        'participant_id': {
            'type': 'string',
            'description': 'id for the participant',
        },
        'participant_name': {
            'type': ['string', 'null'],
            'description': 'name for the participant',
        },
        "purpose": {
            'type': ['string', 'null'],
            'description': 'participant purpose'
        },
        "sessions": {
            'type': ['array', 'null'],
            'items': session
        },
        "user_id": {
            'type': ['string', 'null'],
            'description': 'Unique identifier for the user'
        }
    }
}

conversation = {
    'type': 'object',
    'properties': {
        'conversation_id': {
            'type': 'string',
            'description': 'id for the conversation',
        },
        'conversation_start': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'start timestamp for the conversation',
        },
        'conversation_end': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'end timestamp for the conversation',
        },
        'division_ids': {
            'type': ['array', 'null'],
            'items': {
                'type': ["null", "string"]
            },
            'description': 'division ids'
        },
        'media_stats_min_conversation_mos': {
            'type': ['number', 'null'],
            'description': 'mediaStatsMinConversationMos'
        },
        'media_stats_min_conversation_r_factor': {
            'type': ['number', 'null'],
            'description': 'mediaStatsMinConversationRFactor'
        },
        'originating_direction': {
            'type': ['string', 'null'],
            'description': 'originatingDirection'
        },
        'participants': {
            'type': ['array', 'null'],
            'items': participant
        }
    }
}


user_state = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the user state',
        },
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        },
        'start_time': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'start time',
        },
        'end_time': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'end time',
        },
        'state': {
            'type': 'string',
            'description': 'state'
        },
        'state_id': {
            'type': ['string', 'null'],
            'description': 'state id'
        },
        'type': {
            'type': 'string',
            'description': 'message type'
        }
    }
}

management_unit = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the management unit',
        },
        'name': {
            'type': 'string',
            'description': 'name for the management unit',
        }
    }
}

activity_code = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'id for the activity code',
        },
        'management_unit_id': {
            'type': 'string',
            'description': 'id for the management unit for this activity code',
        },
        'name': {
            'type': 'string',
            'description': 'name for this activity code',
        },
        'category': {
            'type': 'string',
            'description': 'category for this activity code',
        }
    }
}

management_unit_users = {
    'type': 'object',
    'properties': {
        'management_unit_id': {
            'type': 'string',
            'description': 'id for the management unit for this user',
        },
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        }
    }
}

user_schedule_shifts_activities = {
    'type': 'object',
    'properties': {
        'activity_code_id': {
            'type': 'string',
            'description': 'id for the activity_code',
        }
    }
}

user_schedule_shifts = {
    'type': 'object',
    'properties': {
        'start_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'date for the shift',
        },
        'activities': {
            'type': ['array', 'null'],
            'items': user_schedule_shifts_activities
        }
    }
}

user_schedule = {
    'type': 'object',
    'properties': {
        'user_id': {
            'type': 'string',
            'description': 'id for the user',
        },
        'start_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'date for the sync',
        },
        'shifts': {
            'type': ['array', 'null'],
            'items': user_schedule_shifts
        }
    }
}

presence_label = {
    'type': 'object',
    'properties': {
        'en_US': {
            'type': 'string',
            'description': 'English presence label'
        }
    }
}

presence = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'presence id',
        },
        'language_labels': presence_label,
        'created_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'presence creation date',
        },
        'modified_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'presence modification date',
        }
    }
}

queue = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'queue id',
        },
        'name': {
            'type': 'string',
            'name': 'queue name',
        },
        'member_count': {
            'type': 'number',
            'name': 'queue member count',
        },
        'created_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'queue creation date',
        },
        'modified_date': {
            'type': ['string', 'null'],
            'format': 'date-time',
            'description': 'queue modification date',
        }
    }
}

queue_membership = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'id for the user membership in this queue',
        },
        'queue_id': {
            'type': 'string',
            'name': 'id for the queue',
        },
        'user_id': {
            'type': 'string',
            'name': 'user id for this queue',
        }
    }
}

queue_wrapup = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'id for the wrapup code in this queue',
        },
    }
}

division = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'name': 'id of the division'
        },
        'name': {
            'type': ['string', 'null'],
            'description': 'division name'
        },
        'self_uri': {
            'type': ['string', 'null'],
            'description': 'self url'
        }
    }
}

campaign = {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'string',
            'description': 'campaign id'
        },
        'name': {
            'type': ['string', 'null'],
            'description': 'campaign name'
        },
        'dialing_mode': {
            'type': ['string', 'null'],
            'description': 'dialing mode'
        },
        'campaign_status': {
            'type': ['string', 'null'],
            'description': 'campaign status'
        },
        'priority': {
            'type': ['number', 'null'],
            'description': 'priority'
        },
        'no_answer_timeout': {
            'type': ['number', 'null'],
            'description': 'no answer timeout'
        },
        'queue': {
            'type': ['object', 'null'],
            'properties': {
                'id': {
                    'type': ['null', 'string'],
                    'description': 'queue id for reference'
                }
            }
        },
        'division': {
            'type': ['object', 'null'],
            'properties': {
                'id': {
                    'type': ['null', 'string'],
                    'description': 'division id for reference'
                }
            }
        }
    }
}
