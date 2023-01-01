from opentelemetry import trace

import requests
from opentelemetry import metrics
from opentelemetry.trace import Status, StatusCode
# from opentelemetry.sdk.metrics.export.controller import PushController
# from opentelemetry.ext.otcollector.metrics_exporter import CollectorMetricsExporter
# # from opentelemetry.ext.prometheus import PrometheusMetricsExporter
# # from opentelemetry.sdk.metrics import Counter, MeterProvider
# # from opentelemetry.sdk.metrics.export.controller import PushController
# # from prometheus_client import start_http_server


from fastapi import FastAPI

# Acquire a tracer
tracer = trace.get_tracer(__name__)

# Acquire a meter.
meter = metrics.get_meter(__name__)

# Now create a counter instrument to make measurements with
square_counter = meter.create_counter(
    "square_counter",
    description="The number of times sqaure function is called",
)

validate_counter = meter.create_counter(
    "validate_counter",
    description="The number of times validate function is called",
)

# collector_exporter = CollectorMetricsExporter(
#     endpoint="otel-collector:55678"
# )
# controller = PushController(meter, collector_exporter, 5)

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello from find-square app"



@app.get("/calculateSqaure/{number}")
def calculate_square(number):
    val =  validate(number)
    if val == 0:
        current_span = trace.get_current_span()
        current_span.set_status(Status(StatusCode.ERROR))
        return str(number) + " is invalid, provide an integer value"
    else:
        response = requests.post(url="http://traffic-distributor:5001/distribute/" + str(number))
        return response.text


def validate(id):
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("validate") as validatespan:  
        validatespan.set_attribute("validate.value", id)
        # This adds 1 to the counter
        validate_counter.add(1)
        try:
             int(id)
             return 1
        except ValueError:
            return 0