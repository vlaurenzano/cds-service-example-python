import cds_hooks_work as cds
import os

debug = os.environ.get('DEBUG', False)

app = cds.App()


def greeting(r: cds.PatientViewRequest) -> cds.Response:
    resp = cds.Response()
    resp.cards = [cds.Card.info("hello world!", "demo_service")]
    return resp


service = cds.Service.patient_view("myid", "mydesc", greeting)

app.register_service(service)

def serve(environ, start_response):
    print(environ, start_response)
    cds.serve(app, host='0.0.0.0', debug=debug)

if __name__ == '__main__':
   serve("direct", "starting from local")

