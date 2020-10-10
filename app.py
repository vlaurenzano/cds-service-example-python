import cds_hooks_work as cds
import os

debug = os.environ.get('DEBUG', False)

cds_app = cds.App()


def greeting(r: cds.PatientViewRequest) -> cds.Response:
    resp = cds.Response()
    resp.cards = [cds.Card.info("hello world!", "demo_service")]
    return resp


service = cds.Service.patient_view("myid", "mydesc", greeting)

cds_app.register_service(service)

def app(*args, **kwargs):

    port = os.environ.get("PORT", 5000)
    cds.serve(cds_app, host='0.0.0.0', port=port, debug=debug)


if __name__ == '__main__':
    app()

