import logging

import azure.functions as func


def main(req: func.HttpRequest, recommendations: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not recommendations or len(recommendations) == 0:
        logging.warning("Recommendation item not found")
        return func.HttpResponse(
            "Recommendation item not found",
            status_code=404,
        )

    return func.HttpResponse(
        recommendations[0].to_json(),
        mimetype="application/json",
        status_code=200,
    )
