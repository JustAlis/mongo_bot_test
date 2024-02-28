from datetime import datetime
from .connection import collection

def get_db_values(aggregation_type: str, dt_from: str, dt_upto: str):

    if aggregation_type == "day":
        format_date = "%Y-%m-%dT00:00:00"
    elif aggregation_type == "hour":
        format_date = "%Y-%m-%dT%H:00:00"
    elif aggregation_type == "month":
        format_date = "%Y-%m-01T00:00:00"
    else:
        raise ValueError("Неподдерживаемый тип агрегации")
    
    iso_dt_from = datetime.fromisoformat(dt_from)
    iso_dt_upto = datetime.fromisoformat(dt_upto)

    pipeline = [
        {
            "$match": {
                "dt": {
                    "$gte": iso_dt_from,
                    "$lte": iso_dt_upto
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "$dateToString": {
                        "format": format_date,
                        "date": "$dt"
                    }
                },
                "total_value": {"$sum": "$value"}
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        },
        {
            "$group": {
                "_id": None,
                "dataset": {"$push": "$total_value"},
                "labels": {"$push": "$_id"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "dataset": 1,
                "labels": 1
            }
        }
    ]

    result = list(collection.aggregate(pipeline))
    return (result[0].get('dataset'), result[0].get('labels'))